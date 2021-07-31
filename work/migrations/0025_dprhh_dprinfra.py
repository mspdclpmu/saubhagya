# Generated by Django 2.2.6 on 2019-11-06 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0024_auto_20191106_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='DprInfra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ht_length', models.FloatField(blank=True, null=True)),
                ('lt3_length', models.FloatField(blank=True, null=True)),
                ('lt1_length', models.FloatField(blank=True, null=True)),
                ('dtr100_no', models.IntegerField(blank=True, null=True)),
                ('dtr63_no', models.IntegerField(blank=True, null=True)),
                ('dtr25_no', models.IntegerField(blank=True, null=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='work.Site')),
            ],
        ),
        migrations.CreateModel(
            name='DprHH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('mode', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('hh_bpl', models.IntegerField(blank=True, null=True)),
                ('hh_bpl_metered', models.IntegerField(blank=True, null=True)),
                ('hh_metered', models.IntegerField(blank=True, null=True)),
                ('hh_unmetered', models.IntegerField(blank=True, null=True)),
                ('hh_apl_free', models.IntegerField(blank=True, null=True)),
                ('hh_apl_not_free', models.IntegerField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='work.Site')),
            ],
        ),
    ]
