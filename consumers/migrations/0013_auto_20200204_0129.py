# Generated by Django 2.2.6 on 2020-02-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0012_auto_20200131_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='consumer_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
