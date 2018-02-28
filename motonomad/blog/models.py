from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from motonomad.base.blocks import BaseStreamBlock


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items', on_delete=models.CASCADE)


class BlogPage(Page):
    parent_page_types = ['BlogIndexPage']
    subpage_types = []

    tease = RichTextField(blank=True)
    body = RichTextField()
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('tease'),
        StreamFieldPanel('body', classname='full'),
        FieldPanel('tags')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.RelatedFields('tags', [
            index.SearchField('name'),
        ])
    ]


class BlogIndexPage(Page):
    subpage_types = [BlogPage, 'cms.ContentPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        posts = BlogPage.objects.live().order_by('-first_published_at')
        paginator = Paginator(posts, 20)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context


