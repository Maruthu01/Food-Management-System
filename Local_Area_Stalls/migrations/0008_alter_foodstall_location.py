# Generated by Django 5.1.1 on 2024-11-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Local_Area_Stalls', '0007_foodstall_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodstall',
            name='Location',
            field=models.URLField(max_length=500),
        ),
    ]