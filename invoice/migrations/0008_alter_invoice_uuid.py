# Generated by Django 4.0.6 on 2022-08-10 20:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e5d418ac-f7ec-4377-96a8-b6b40391e8e0')),
        ),
    ]
