# Generated by Django 2.2.6 on 2019-10-27 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HRQuestions', '0003_auto_20191027_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='first_name',
            field=models.CharField(max_length=64, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='last_name',
            field=models.CharField(max_length=64, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Rekruter'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(verbose_name='Treść'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Dodano'),
        ),
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRQuestions.Language', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('junior', 'junior'), ('mid', 'mid'), ('senior', 'senior')], max_length=10, verbose_name='Poziom'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('definition', 'definition'), ('exercise', 'exercise')], max_length=10, verbose_name='Typ pytania'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='questionlist',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Nazwa'),
        ),
    ]
