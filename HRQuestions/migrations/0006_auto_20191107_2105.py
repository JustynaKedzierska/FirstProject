# Generated by Django 2.2.6 on 2019-11-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRQuestions', '0005_auto_20191030_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Tytuł'),
        ),
    ]
