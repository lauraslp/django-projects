# Generated by Django 4.0 on 2022-07-02 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='microchip',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('CAT', 'Cat'), ('DOG', 'Dog'), ('RABBIT', 'Rabbit')], max_length=20),
        ),
        migrations.AlterField(
            model_name='visit',
            name='anestesia',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='visit',
            name='drug_id',
            field=models.CharField(choices=[('ANTIPARASITIS', 'Antiparasitis'), ('ANTIFUNGALS', 'Antifungal'), ('STEROIDS', 'Steroids'), ('PAIN RELIEVES', 'Pain Relieves')], max_length=100),
        ),
        migrations.AlterField(
            model_name='visit',
            name='treatment',
            field=models.CharField(choices=[('MEDICA', 'Medical'), ('SURGICAL', 'Surgical'), ('OTHER', 'Other')], max_length=10),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vetapp.client')),
                ('Pet_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vetapp.pet')),
                ('Visit_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vetapp.visit')),
            ],
        ),
    ]
