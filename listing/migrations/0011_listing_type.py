# Generated by Django 3.0.6 on 2020-09-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_auto_20200831_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Type',
            field=models.CharField(default='hostel', max_length=255),
        ),
    ]
