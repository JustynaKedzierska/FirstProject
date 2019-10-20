from django.contrib.auth.models import User, Group
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView

from HRQuestions.models import Question, Language, QuestionList


class IndexView(View):
    pass


class UserCreateView(CreateView):
    template_name = 'AUTH/add_user_form.html'
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('index')


class UserListView(ListView):
    model = User
    paginate_by = 10


class QuestionCreateView(CreateView):
    template_name = 'question_create.html'
    model = Question
    fields = ['title', 'author', 'language', 'question_type', 'level', 'content']
    success_url = reverse_lazy('question-list')


class QuestionListView(ListView):
    model = Question
    paginate_by = 10


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['title', 'question_type', 'level', 'language', 'content']
    template_name_suffix = '_update_form'


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('question-list')


class LanguageCreateView(CreateView):
    template_name = 'language_create.html'
    model = Language
    fields = ['name']
    success_url = reverse_lazy('language-list')


class LanguageListView(ListView):
    model = Language
    paginate_by = 10


class LanguageUpdateView(UpdateView):
    model = Language
    fields = ['name']
    template_name_suffix = '_update_form'


class LanguageDeleteView(DeleteView):
    model = Language
    success_url = reverse_lazy('language-list')


class QuestionListCreateView(CreateView):
    template_name = 'question_list_create.html'
    model = QuestionList
    fields = ['name', 'author', 'question']
    success_url = reverse_lazy('question-list')


class QuestionListListView(ListView):
    model = QuestionList
    paginate_by = 10
