from django import template
from page.models import ExternalAccount

register = template.Library()

...

# ExternalAccount snippets
@register.inclusion_tag('tags/external_account.html', takes_context=True)
def external_accounts(context):
    return {
        'external_accounts': ExternalAccount.objects.all(),
        'request': context['request'],
    }