# Generated by Django 5.1.2 on 2025-01-26 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('emp_code', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.position')),
            ],
        ),
    ]
