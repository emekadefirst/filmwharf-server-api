# Generated by Django 5.0.1 on 2024-01-19 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HashTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=350)),
                ('download_link', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=250)),
                ('release_date', models.DateTimeField(default=None)),
                ('thumbnail_url', models.CharField(max_length=1000)),
                ('Trailer_url', models.CharField(max_length=1000)),
                ('director', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hashtags')),
            ],
        ),
    ]
