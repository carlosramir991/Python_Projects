# Generated by Django 3.1.2 on 2020-10-31 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_auto_20201031_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='djangoclasses',
            old_name='instructor_name',
            new_name='name',
        ),
    ]
