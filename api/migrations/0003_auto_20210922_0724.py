# Generated by Django 3.2.7 on 2021-09-22 07:24

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='fame',
            field=picklefield.fields.PickledObjectField(default=[], editable=False),
        ),
        migrations.AddField(
            model_name='book',
            name='fame',
            field=picklefield.fields.PickledObjectField(default=[], editable=False),
        ),
    ]