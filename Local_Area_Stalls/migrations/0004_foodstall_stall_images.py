# Generated by Django 5.1.1 on 2024-11-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Local_Area_Stalls', '0003_foodstall_contact_num_alter_foodstall_closing_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodstall',
            name='Stall_images',
            field=models.ImageField(default=1, upload_to='stall_images/'),
            preserve_default=False,
        ),
    ]