# Generated by Django 3.0.6 on 2020-06-17 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200615_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
    ]