# Generated by Django 2.2.6 on 2019-12-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0052_siteextra_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressqty',
            name='review',
            field=models.CharField(blank=True, choices=[('ok', 'ok'), ('issue', 'issue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='progressqtyextra',
            name='review',
            field=models.CharField(blank=True, choices=[('ok', 'ok'), ('issue', 'issue')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='progressqtyextra',
            name='status',
            field=models.CharField(blank=True, choices=[('completed', 'completed'), ('ongoing', 'ongoing'), ('not started', 'not started'), ('canceled', 'canceled')], max_length=200, null=True),
        ),
    ]