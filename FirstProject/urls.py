"""HRquestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from HRQuestions.views import UserCreateView, QuestionCreateView, LanguageCreateView, LanguageListView, \
    LanguageUpdateView, QuestionListView, QuestionUpdateView, LanguageDeleteView, QuestionListCreateView, UserListView, \
    QuestionListListView, QuestionDeleteView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    url(r'^user/add', UserCreateView.as_view(), name='user-add'),
    url(r'^user/list', UserListView.as_view(), name='user-list'),
    url(r'^question/add', QuestionCreateView.as_view(), name='question-add'),
    url(r'^question/list', QuestionListView.as_view(), name='question-list'),
    url(r'^question/update/(?P<pk>(\d)+)', QuestionUpdateView.as_view(), name='question-update'),
    url(r'^question/delete/(?P<pk>(\d)+)', QuestionDeleteView.as_view(), name='question-delete'),
    url(r'^language/add', LanguageCreateView.as_view(), name='language-add'),
    url(r'^language/list', LanguageListView.as_view(), name='language-list'),
    url(r'^language/update/(?P<pk>(\d)+)', LanguageUpdateView.as_view(), name='language-update'),
    url(r'^language/delete/(?P<pk>(\d)+)', LanguageDeleteView.as_view(), name='language-delete'),
    url(r'^question_group/add', QuestionListCreateView.as_view(), name='question-group-add'),
    url(r'^question_group/list', QuestionListListView.as_view(), name='question-group-list'),
]
