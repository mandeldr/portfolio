# Generated by Django 3.0.6 on 2020-05-19 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200518_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrument',
            old_name='owner',
            new_name='portfolio',
        ),
    ]