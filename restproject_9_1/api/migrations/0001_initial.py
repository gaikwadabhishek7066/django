# Generated by Django 5.1.2 on 2025-01-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('fee', models.FloatField()),
            ],
        ),
    ]
