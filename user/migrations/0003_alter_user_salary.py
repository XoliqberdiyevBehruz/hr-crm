# Generated by Django 4.2 on 2025-03-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_date_of_birth_alter_user_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
