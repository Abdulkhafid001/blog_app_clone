# Generated by Django 5.1.5 on 2025-01-30 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogPost',
        ),
    ]
