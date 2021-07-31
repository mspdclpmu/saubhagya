# Generated by Django 2.2.6 on 2019-12-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0070_auto_20191213_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=50)),
                ('variantof', models.ManyToManyField(related_name='_variations_variantof_+', to='work.Variations')),
            ],
        ),
    ]
