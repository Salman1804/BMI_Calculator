# Generated by Django 4.0.2 on 2022-09-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('Height', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('Calculate_BMI', models.IntegerField()),
            ],
        ),
    ]
