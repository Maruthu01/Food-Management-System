# Generated by Django 5.1.1 on 2024-12-02 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Local_Area_Stalls', '0011_icecreamstall_juicestall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icecreamstall',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='juicestall',
            name='ratings',
        ),
    ]
