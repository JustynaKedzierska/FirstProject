from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
QUESTION_TYPE = (
    ('definition', 'definition'),
    ('exercise', 'exercise'),
)

LEVEL = (
    ('junior', 'junior'),
    ('mid', 'mid'),
    ('senior', 'senior'),

)


class Language(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    question_type = models.CharField(choices=QUESTION_TYPE, max_length=10)
    level = models.CharField(choices=LEVEL, max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title


class QuestionList(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Interview(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date = models.DateField()



