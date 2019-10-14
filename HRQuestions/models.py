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
    ('min', 'mid'),
    ('senior', 'senior'),

)

PUBLIC = (
    ('yes', 'yes'),
    ('true', 'true'),

)


class Language(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Question(models.Model):
    tittle = models.CharField(max_length=64)
    content = models.TextField()
    question_type = models.CharField(choices=QUESTION_TYPE, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    level = models.CharField(choices=LEVEL, max_length=10)
    group = models.ManyToManyField('Group')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    public = models.CharField(choices=PUBLIC, max_length=10)

    def __str__(self):
        return self.tittle


class Group(models.Model):
    name = models.CharField(max_length=64)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
