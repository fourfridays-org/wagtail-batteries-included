from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models import Count, Q
from django.template.defaultfilters import slugify
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from page.blocks import BaseStreamBlock

import datetime


@register_snippet
class ArticleCategory(models.Model):
    name = models.CharField(max_length=180, unique=True, verbose_name=_('Article Category Name'), default='')
    slug = models.SlugField(unique=True, max_length=80)
    description = models.CharField(max_length=500, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            count = ArticleCategory.objects.filter(slug=slug).count()
            if count > 0:
                slug = '{}-{}'.format(slug, count)
            self.slug = slug
        return super(ArticleCategory, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['name']
        verbose_name = _("Article Category")
        verbose_name_plural = _("Article Categories")


def limit_author_choices():
    """ Limit choices in article author field based on config settings """
    LIMIT_AUTHOR_CHOICES = getattr(settings, 'NEWS_LIMIT_AUTHOR_CHOICES_GROUP', 'Editors')
    if LIMIT_AUTHOR_CHOICES:
        if isinstance(LIMIT_AUTHOR_CHOICES, str):
            limit = Q(groups__name=LIMIT_AUTHOR_CHOICES)
        else:
            limit = Q()
            for s in LIMIT_AUTHOR_CHOICES:
                limit = limit | Q(groups__name=s)
        if getattr(settings, 'NEWS_LIMIT_AUTHOR_CHOICES_ADMIN', False):
            limit = limit | Q(is_staff=True)
    else:
        limit = {'is_staff': True}
    return limit


class ArticlePageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the ArticlePage object and tags. There's a longer guide on using it at
    http://docs.wagtail.io/en/latest/reference/pages/model_recipes.html#tagging
    """
    content_object = ParentalKey('ArticlePage', related_name='tagged_items', on_delete=models.CASCADE)


class ArticlePage(Page):
    date_published = models.DateField("Date article published", default=datetime.datetime.today)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to=limit_author_choices,
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        related_name='author_pages',
        blank=True, null=True,
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = StreamField(BaseStreamBlock(), verbose_name="Page body", blank=True)
    categories = ParentalManyToManyField('ArticleCategory', blank=True)
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)
    enable_commenting = models.BooleanField(default=False)
    flickr_photoset_id = models.CharField(max_length=25, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date_published'),
        FieldPanel('author'),
        ImageChooserPanel('hero_image'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ]),
        FieldPanel('enable_commenting'),
        FieldPanel('flickr_photoset_id'),
    ]

    def get_context(self, request):
        context = super(ArticlePage, self).get_context(request)
        context['recent_posts'] = ArticlePage.objects.live().exclude(id=self.id).order_by('-date_published')[:3]
        context['tags'] = self.tags.all().order_by('name')
        context['comments'] = self.comments.all().filter(active=True)
        context['comment_count'] = self.comments.all().filter(active=True).count()
        return context

    # Specifies parent to ArticlePage as being ArticleIndexPages
    parent_page_types = ['ArticleIndexPage']

    # Specifies what content types can exist as children of ArticlePage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


class ArticleIndexPage(RoutablePageMixin, Page):
    """
    Index page for articles.
    We need to alter the page model's context to return the child page objects,
    the ArticlePage objects, so that it works as an index page

    RoutablePageMixin is used to allow for a custom sub-URL for the tag views
    defined above.
    """
    introduction = models.TextField(help_text='Text to describe the page', blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('hero_image'),
    ]

    # Speficies that only ArticlePage objects can live under this index page
    subpage_types = ['ArticlePage']

    # Defines a method to access the children of the page (e.g. ArticlePage
    # objects). On the demo site we use this on the HomePage
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(ArticleIndexPage, self).get_context(request)
        context['posts'] = ArticlePage.objects.descendant_of(self).live().order_by('-date_published')
        return context

    # This defines a Custom view that utilizes Tags. This view will return all
    # related ArticlePages for a given Tag or redirect back to the ArticleIndexPage.
    # More information on RoutablePages is at
    # http://docs.wagtail.io/en/latest/reference/contrib/routablepage.html
    @route(r'^tag/$')
    def all_article_tags(self, request):
        tags = ArticlePageTag.objects.all().order_by('tag__name')
        context = { 'tags': tags}
        return render(request, 'tags/article_tags_index_page.html', context)

    @route(r'^tag/([\w-]+)/$')
    def tag_archive(self, request, tag=None):
        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no articles tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        posts = self.get_posts(tag=tag)
        context = {
            'tag': tag,
            'posts': posts
        }
        return render(request, 'tags/article_tag_page.html', context)

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child ArticlePage objects for this ArticlePageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = ArticlePage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this ArticlePage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags


class Comment(models.Model):
    article = models.ForeignKey('ArticlePage', on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.content