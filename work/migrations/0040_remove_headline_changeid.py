# Generated by Django 2.2.6 on 2019-11-25 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0039_auto_20191125_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='changeid',
        ),
    ]