# Generated by Django 4.1.5 on 2023-02-26 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_creater',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='is_procreater',
            field=models.BooleanField(blank=True, default=0),
        ),
    ]
