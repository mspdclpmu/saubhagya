# Generated by Django 3.0.4 on 2020-03-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0098_boq_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='boq',
            name='group',
            field=models.CharField(default='RURAL', max_length=50),
            preserve_default=False,
        ),
    ]
