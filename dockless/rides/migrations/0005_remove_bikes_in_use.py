# Generated by Django 3.2.5 on 2021-08-07 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0004_bikes_in_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikes',
            name='in_use',
        ),
    ]