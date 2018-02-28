from django.db import migrations


def create_homepage(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    BlogIndexPage = apps.get_model('blog.BlogIndexPage')

    Page.objects.filter(pk=2).delete()

    indexpage_content_type, __ = ContentType.objects.get_or_create(
        model='blogindexpage', app_label='blog')

    homepage = BlogIndexPage.objects.create(
        title='Блог о путешествиях',
        draft_title='Блог о путешествиях',
        slug='',
        content_type=indexpage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/',
    )

    Site.objects.create(
        hostname='motonomad.ru', root_page=homepage, is_default_site=True)


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_homepage)
    ]

