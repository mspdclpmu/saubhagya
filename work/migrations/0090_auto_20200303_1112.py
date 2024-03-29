# Generated by Django 2.2.6 on 2020-03-03 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0089_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsurveyqty',
            name='diverted_to',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='work.Site'),
        ),
        migrations.AddField(
            model_name='surveyqty',
            name='diverted_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diversion', to='work.Site'),
        ),
    ]
