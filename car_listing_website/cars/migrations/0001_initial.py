# Generated by Django 4.1.1 on 2022-09-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=30)),
                ('Brand', models.CharField(max_length=30)),
                ('Year', models.IntegerField()),
            ],
        ),
    ]
