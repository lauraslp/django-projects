# Generated by Django 4.0 on 2022-07-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetapp', '0007_rename_age_in_year_pet_age_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age_month',
            field=models.IntegerField(null=True),
        ),
    ]
