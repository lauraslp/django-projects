# Generated by Django 4.0 on 2022-07-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_clinic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='clinic',
            field=models.CharField(choices=[('FAST GIRAFFE', 'Fast Giraffe'), ('CARE VET', 'Care Vet'), ('DRPAWPAW', 'DrPawPaw'), ('DR.VET', 'Dr.Vet')], max_length=100),
        ),
    ]
