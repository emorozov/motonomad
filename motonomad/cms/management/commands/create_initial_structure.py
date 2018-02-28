from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

from wagtail.core.models import Page

from motonomad.cms.models import ContentPage


class Command(BaseCommand):
    help = 'Create initial pages required for functional blog'

    def handle(self, *args, **kwargs):
        root_page = Page.objects.get(url_path='/', depth=2)

        page_content_type = ContentType.objects.get(model='contentpage', app_label='cms')
        about = ContentPage(
            title='Об авторе',
            draft_title='Об авторе',
            slug='about',
            content_type=page_content_type,
            show_in_menus=True,
        )
        root_page.add_child(instance=about)

        feedback = ContentPage(
            title='Обратная связь',
            draft_title='Обратная связь',
            slug='feedback',
            content_type=page_content_type,
            show_in_menus=True,
        )
        root_page.add_child(instance=feedback)

