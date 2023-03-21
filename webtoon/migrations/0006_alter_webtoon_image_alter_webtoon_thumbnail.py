# Generated by Django 4.1.5 on 2023-03-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0005_alter_webtoon_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtoon',
            name='image',
            field=models.ImageField(blank=True, upload_to='webtoon/{author_uid}'),
        ),
        migrations.AlterField(
            model_name='webtoon',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='webtoonthumnail/{author_uid}'),
        ),
    ]
