# Generated by Django 4.2.17 on 2025-01-29 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0006_reservation_staff_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservations_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
