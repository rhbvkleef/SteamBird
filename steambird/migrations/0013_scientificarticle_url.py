# Generated by Django 2.1.8 on 2019-06-13 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steambird', '0012_auto_20190612_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientificarticle',
            name='url',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Possible URL to the Article'),
        ),
    ]