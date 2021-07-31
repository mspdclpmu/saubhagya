# Generated by Django 2.2.6 on 2019-11-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0020_auto_20191105_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dprinfra',
            old_name='dtr_no',
            new_name='dtr100_no',
        ),
        migrations.RenameField(
            model_name='dprinfra',
            old_name='lt_length',
            new_name='lt1_length',
        ),
        migrations.RemoveField(
            model_name='dprinfra',
            name='dtr_material',
        ),
        migrations.RemoveField(
            model_name='dprinfra',
            name='ht_material',
        ),
        migrations.RemoveField(
            model_name='dprinfra',
            name='lt_material',
        ),
        migrations.AddField(
            model_name='dprinfra',
            name='dtr25_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dprinfra',
            name='dtr63_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dprinfra',
            name='lt3_length',
            field=models.FloatField(blank=True, null=True),
        ),
    ]