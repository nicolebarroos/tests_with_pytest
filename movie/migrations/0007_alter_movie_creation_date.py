# Generated by Django 4.0.3 on 2022-03-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_rename_date_movie_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
