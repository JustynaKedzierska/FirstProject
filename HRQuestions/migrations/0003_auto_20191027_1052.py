# Generated by Django 2.2.6 on 2019-10-27 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HRQuestions', '0002_auto_20191019_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionlist',
            old_name='question',
            new_name='questions',
        ),
    ]
