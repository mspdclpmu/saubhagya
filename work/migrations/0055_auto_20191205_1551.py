# Generated by Django 2.2.6 on 2019-12-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0054_auto_20191203_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progressqty',
            name='review',
        ),
        migrations.RemoveField(
            model_name='progressqtyextra',
            name='review',
        ),
        migrations.AddField(
            model_name='progressqty',
            name='review_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='progressqtyextra',
            name='review_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
