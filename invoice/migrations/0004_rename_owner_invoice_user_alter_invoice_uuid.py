# Generated by Django 4.0.6 on 2022-08-10 01:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('29d39771-54ff-49d9-b25c-742e2ebcd173')),
        ),
    ]
