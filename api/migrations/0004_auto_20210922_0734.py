# Generated by Django 3.2.7 on 2021-09-22 07:34

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210922_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fame',
            field=picklefield.fields.PickledObjectField(default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='fame',
            field=picklefield.fields.PickledObjectField(default=list, editable=False),
        ),
    ]