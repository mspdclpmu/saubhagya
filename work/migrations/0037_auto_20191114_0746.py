# Generated by Django 2.2.6 on 2019-11-14 07:46

from django.db import migrations, models
import work.models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0036_dprqty_has_infra'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressqty',
            name='document',
            field=models.FileField(null=True, upload_to=work.models.habCompletionDocPath),
        ),
        migrations.AddField(
            model_name='progressqtyextra',
            name='document',
            field=models.FileField(null=True, upload_to=work.models.habCompletionDocPath),
        ),
    ]