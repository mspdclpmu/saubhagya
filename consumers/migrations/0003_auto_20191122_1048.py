# Generated by Django 2.2.6 on 2019-11-22 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0002_auto_20191122_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='work.Site'),
        ),
    ]