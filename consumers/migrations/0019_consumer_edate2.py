# Generated by Django 2.2.6 on 2021-04-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0018_consumer_cinfra_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='edate2',
            field=models.DateField(blank=True, null=True),
        ),
    ]