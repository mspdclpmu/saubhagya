# Generated by Django 2.2.6 on 2019-12-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0008_consumer_hab_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='district',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]