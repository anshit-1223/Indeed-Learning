# Generated by Django 4.2.11 on 2024-04-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fsignup',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('passwd', models.CharField(max_length=10)),
                ('fid', models.IntegerField()),
            ],
        ),
    ]
