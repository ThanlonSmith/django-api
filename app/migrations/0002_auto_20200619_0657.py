# Generated by Django 3.0.7 on 2020-06-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
