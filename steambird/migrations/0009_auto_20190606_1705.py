# Generated by Django 2.1.8 on 2019-06-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steambird', '0008_auto_20190520_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(default=-1, max_length=256, verbose_name='Edition of the book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='msp',
            name='mandatory',
            field=models.BooleanField(default=True, verbose_name='Is the material mandatory?'),
        ),
    ]
