# Generated by Django 2.2.6 on 2019-11-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0019_auto_20191105_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dprhh',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]