# Generated by Django 4.0 on 2022-07-09 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetapp', '0005_pet_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='age',
            new_name='age_in_year',
        ),
    ]
