# Generated by Django 3.0.3 on 2020-03-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviepredict', '0002_auto_20200318_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='runtime',
            new_name='name',
        ),
    ]
