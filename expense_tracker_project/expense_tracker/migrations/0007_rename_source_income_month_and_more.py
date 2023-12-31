# Generated by Django 5.0 on 2024-01-05 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0006_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='source',
            new_name='month',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='amount',
            new_name='monthly_salary',
        ),
        migrations.RemoveField(
            model_name='income',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='income',
            name='date',
        ),
        migrations.RemoveField(
            model_name='income',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='income',
            name='user',
        ),
    ]
