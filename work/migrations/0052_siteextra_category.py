# Generated by Django 2.2.6 on 2019-12-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0051_auto_20191202_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteextra',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
