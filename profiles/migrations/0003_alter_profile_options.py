# Generated by Django 3.2.16 on 2022-10-29 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_profiles_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created_at'], 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
    ]
