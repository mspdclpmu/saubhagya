# Generated by Django 2.2.6 on 2019-11-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0044_auto_20191129_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='census',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='census',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]