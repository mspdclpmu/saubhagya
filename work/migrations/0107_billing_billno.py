# Generated by Django 2.2.6 on 2020-04-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0106_auto_20200407_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='billno',
            field=models.TextField(blank=True, null=True),
        ),
    ]
