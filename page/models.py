from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import ImageGridBlock, BaseStreamBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock, HeroImageBlock


@register_snippet
class ExternalAccount(models.Model):
    EXTERNAL_PROFILE_CHOICES = [
        ('facebook', 'Facebook'),
        ('flickr', 'Flickr'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
    ]
    account = models.CharField(max_length=20, choices=EXTERNAL_PROFILE_CHOICES, default='instagram')
    url = models.URLField(default='')

    def __str__(self):
        return self.account


class StandardPage(Page):
    body = StreamField([
        ('hero_image', HeroImageBlock(icon='image')),
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ],default='')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]