from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from motonomad.base.blocks import BaseStreamBlock


class ContentPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname='full'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

