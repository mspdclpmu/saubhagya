# Generated by Django 2.2.6 on 2019-12-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0007_consumer_village'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='hab_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]