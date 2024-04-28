# Generated by Django 4.1.4 on 2022-12-21 13:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0006_examination_system_alter_downloads_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('answer', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]