# Generated by Django 4.1.4 on 2022-12-21 10:32

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0004_downloads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloads',
            name='desc',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
