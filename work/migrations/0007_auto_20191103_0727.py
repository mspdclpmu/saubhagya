# Generated by Django 2.2.6 on 2019-11-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_auto_20191103_0425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='ref_id',
            new_name='approve_id',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='site_id',
            new_name='hab_id',
        ),
    ]