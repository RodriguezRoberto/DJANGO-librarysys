# Generated by Django 4.0.6 on 2022-08-21 00:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0017_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('bc0808d2-7ab0-4d40-93f8-9bc6674b48c2')),
        ),
    ]
