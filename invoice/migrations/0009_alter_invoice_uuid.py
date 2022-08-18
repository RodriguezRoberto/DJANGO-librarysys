# Generated by Django 4.0.6 on 2022-08-10 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('fd273bd5-2db9-43ce-ba07-eaf15ab34da3')),
        ),
    ]