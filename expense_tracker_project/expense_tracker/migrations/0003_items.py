# Generated by Django 5.0 on 2024-01-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0002_remove_expense_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=255)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Date', models.DateField()),
            ],
        ),
    ]