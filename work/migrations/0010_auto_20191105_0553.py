# Generated by Django 2.2.6 on 2019-11-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_auto_20191103_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='hab_id',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together=set(),
        ),
    ]