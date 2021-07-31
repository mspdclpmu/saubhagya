# Generated by Django 2.2.6 on 2020-01-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0083_auto_20200110_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalresolution',
            name='status',
            field=models.CharField(blank=True, choices=[('done', 'done'), ('pending', 'pending'), ('deferred', 'deferred'), ('info', 'info')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='status',
            field=models.CharField(blank=True, choices=[('done', 'done'), ('pending', 'pending'), ('deferred', 'deferred'), ('info', 'info')], max_length=10, null=True),
        ),
    ]
