# Generated by Django 5.0 on 2024-01-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0002_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.SmallIntegerField(),
        ),
    ]
