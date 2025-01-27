# Generated by Django 5.1.2 on 2025-01-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('dpt_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=20)),
                ('dpt', models.CharField(max_length=10)),
                ('salary', models.CharField(max_length=20)),
            ],
        ),
    ]
