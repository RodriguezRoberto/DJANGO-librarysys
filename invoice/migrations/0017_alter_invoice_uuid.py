# Generated by Django 4.0.6 on 2022-08-11 20:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0016_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9e2f4b13-6dd9-4265-b548-9e7f5d600ca7')),
        ),
    ]
