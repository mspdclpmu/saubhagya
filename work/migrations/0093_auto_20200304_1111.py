# Generated by Django 2.2.6 on 2020-03-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0092_auto_20200303_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsiteextra',
            name='is_divertion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='siteextra',
            name='is_divertion',
            field=models.BooleanField(default=False),
        ),
    ]