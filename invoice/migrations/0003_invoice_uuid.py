# Generated by Django 4.0.6 on 2022-08-10 01:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c3f5ec85-37e2-4fa5-b0e6-3c4efeb13e62')),
        ),
    ]