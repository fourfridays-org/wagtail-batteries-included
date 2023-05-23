# Generated by Django 4.2.1 on 2023-05-20 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('article', '0004_authors_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.RenameField(
            model_name='articlepeoplerelationship',
            old_name='authors',
            new_name='author',
        ),
    ]
