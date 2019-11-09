from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
QUESTION_TYPE = (
    ('definition', 'definicja'),
    ('exercise', 'zadanie'),
)

LEVEL = (
    ('junior', 'junior'),
    ('mid', 'mid'),
    ('senior', 'senior'),

)


class Language(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa')

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=256, verbose_name='Tytuł')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Dodano')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Język')
    question_type = models.CharField(choices=QUESTION_TYPE, max_length=10, verbose_name='Typ pytania')
    level = models.CharField(choices=LEVEL, max_length=10, verbose_name='Poziom')
    content = models.TextField(verbose_name='Treść')

    def __str__(self):
        return self.title


class QuestionList(models.Model):
    name = models.CharField(max_length=64, verbose_name='Nazwa')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name


class Interview(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Rekruter')
    first_name = models.CharField(max_length=64, verbose_name='Imię')
    last_name = models.CharField(max_length=64, verbose_name='Nazwisko')
    date = models.DateField(verbose_name='Data')





