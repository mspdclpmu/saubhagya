# Generated by Django 2.2.6 on 2019-11-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0018_dprhh_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='dprhh',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dprhh',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dprhh',
            name='mode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dprhh',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dprhh',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dprinfra',
            name='dtr_material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dprinfra',
            name='ht_material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dprinfra',
            name='lt_material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='progressqtyextra',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='approve_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='block',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='census',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='site',
            name='district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='division',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='hab_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='habitation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='village',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='approve_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='census',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='division',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='hab_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='habitation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteextra',
            name='village',
            field=models.CharField(max_length=50),
        ),
    ]
