# Generated by Django 4.0.6 on 2022-08-10 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_item', '0002_rename_bookitem_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='origin',
            new_name='book',
        ),
    ]
