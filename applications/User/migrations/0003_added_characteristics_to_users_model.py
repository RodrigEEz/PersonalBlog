# Generated by Django 3.2.4 on 2021-07-26 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_added_characteristics_to_users_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
