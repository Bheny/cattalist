# Generated by Django 3.0.6 on 2020-08-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_1', models.PositiveIntegerField(blank=True, default=0)),
                ('star_2', models.PositiveIntegerField(blank=True, default=0)),
                ('star_3', models.PositiveIntegerField(blank=True, default=0)),
                ('star_4', models.PositiveIntegerField(blank=True, default=0)),
                ('star_5', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
