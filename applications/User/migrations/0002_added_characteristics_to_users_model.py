# Generated by Django 3.2.4 on 2021-07-26 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_UserModel_Creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_names',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_names',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
