# Generated by Django 2.2.6 on 2020-06-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0013_auto_20200204_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='census',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='consumer_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='x'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]