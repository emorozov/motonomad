from django.contrib.syndication.views import Feed

from .models import BlogPage


class LatestEntriesFeed(Feed):
    def title(self):
        return 'Лента обновлений блога мотономада'

    def description(self):
        return 'Последние публикации и обновления блога мотономада'

    def link(self):
        return '/'

    def items(self):
        return BlogPage.objects.live().order_by('-last_published_at')[:10]

    def item_author_name(self, item):
        return "Евгений Морозов"

    def item_pubdate(self, item):
        return item.first_published_at

    def item_link(self, item):
        return item.url

    def item_categories(self, item):
        return item.tags.all()

