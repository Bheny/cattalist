# Generated by Django 3.0.6 on 2020-09-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
