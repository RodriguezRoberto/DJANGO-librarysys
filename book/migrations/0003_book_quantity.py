# Generated by Django 4.0.6 on 2022-08-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
