# Generated by Django 5.0 on 2024-01-02 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]
