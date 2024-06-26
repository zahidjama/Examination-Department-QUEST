# Generated by Django 4.1 on 2022-12-13 12:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=244)),
                ('appointment', models.CharField(default='', max_length=244)),
                ('desc', ckeditor.fields.RichTextField()),
                ('contact', models.CharField(default='', max_length=255)),
                ('img', models.FileField(default='', upload_to='media/media/static/')),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='msgs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('charge', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('msg', ckeditor.fields.RichTextField()),
                ('img', models.FileField(default='', upload_to='media/media/static/')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('news', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.FileField(default='', upload_to='media/media/static')),
                ('date', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(default='', max_length=255)),
                ('course_desc', ckeditor.fields.RichTextField()),
                ('photo', models.FileField(default='', upload_to='media/media/static')),
                ('date', models.CharField(default='', max_length=255)),
                ('status', models.CharField(default='', max_length=255)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='examapp.category')),
            ],
        ),
    ]
