# Generated by Django 3.0.4 on 2020-03-13 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0101_auto_20200313_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boq',
            old_name='group',
            new_name='region',
        ),
    ]