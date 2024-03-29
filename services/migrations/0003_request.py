# Generated by Django 3.0.6 on 2020-09-29 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0011_listing_type'),
        ('services', '0002_booking_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_room', to='listing.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
