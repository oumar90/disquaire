# Generated by Django 3.1.3 on 2020-11-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201109_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.URLField(verbose_name='image'),
        ),
    ]