# Generated by Django 4.0.5 on 2022-06-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_sfn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(default='github.com/luizAdamchuk'),
        ),
    ]