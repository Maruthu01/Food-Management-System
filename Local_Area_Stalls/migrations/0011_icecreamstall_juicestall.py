# Generated by Django 5.1.1 on 2024-11-28 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Local_Area_Stalls', '0010_alter_foodstall_location'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IcecreamStall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Ice_type', models.CharField(max_length=100)),
                ('Contact_num', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ratings', models.FloatField(max_length=100)),
                ('opening_time', models.CharField(max_length=100)),
                ('closing_time', models.CharField(max_length=100)),
                ('Stall_images', models.ImageField(upload_to='stall_images/')),
                ('Location', models.URLField(default='NIL', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JuiceStall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Juice_type', models.CharField(max_length=100)),
                ('Contact_num', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ratings', models.FloatField(max_length=100)),
                ('opening_time', models.CharField(max_length=100)),
                ('closing_time', models.CharField(max_length=100)),
                ('Stall_images', models.ImageField(upload_to='stall_images/')),
                ('Location', models.URLField(default='NIL', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
