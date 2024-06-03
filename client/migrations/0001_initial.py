# Generated by Django 4.2 on 2024-06-03 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{9,11}$')])),
                ('address', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]