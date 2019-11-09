from django.contrib.auth.models import User
import django_filters

from .models import Question, QuestionList


class QuestionFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Question
        fields = ['language', 'author', 'level', 'question_type']


class QuestionListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = QuestionList
        fields = ['name', 'author']
