# Generated by Django 4.0 on 2022-07-09 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vetapp', '0003_rename_clinic_card_user_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vetapp.client'),
        ),
    ]