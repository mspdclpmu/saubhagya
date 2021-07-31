# Generated by Django 3.0.4 on 2020-03-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0097_auto_20200304_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('qfield', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50)),
                ('qfield', models.CharField(max_length=50)),
                ('rate', models.FloatField()),
            ],
        ),
    ]