from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from django_filters.views import FilterView

from HRQuestions.models import Question, Language, QuestionList
from .filters import QuestionFilter, QuestionListFilter
from .forms import LoginForm, AddUserForm, ResetPasswordForm, QuestionListModelForm, QuestionUpdateModelForm


class HomePageView(TemplateView):
    template_name = 'landing_page.html'


# class IndexView(View):
#     def get(self, request):
#         question_count = Question.objects.all().count()
#         questionlist_count = QuestionList.objects.all().count()
#
#         context = {'question_count': question_count,
#                    'questionlist_count': questionlist_count}
#         return render(request, template_name='index.html', context=context)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['question_count'] = Question.objects.all().count()
        context['questionlist_count'] = QuestionList.objects.all().count()
        context['language_count'] = Language.objects.all().count()
        return context


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'HRQuestions/login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                return render(request, 'HRQuestions/login_form.html', {'form': form})
        else:
            return render(request, 'HRQuestions/login_form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class UserCreateView(CreateView):
    template_name = 'AUTH/add_user_form.html'
    model = User
    form_class = AddUserForm

    success_url = reverse_lazy('index')


class UserListView(ListView):
    model = User
    paginate_by = 10


class QuestionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'question_create.html'
    model = Question
    fields = ['title', 'author', 'language', 'question_type', 'level', 'content']
    success_url = reverse_lazy('question-list')


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    paginate_by = 15
    template_name = 'question_list.html'
    # context_object_name = 'question'
    # queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['question_count'] = Question.objects.count()
        return context


class QuestionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'HRQuestions.update_question'
    model = Question
    fields = ['title', 'question_type', 'level', 'language', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('question-list')


class QuestionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'HRQuestions.delete_question'
    model = Question
    success_url = reverse_lazy('question-list')


class LanguageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'language_create.html'
    model = Language
    fields = ['name']
    success_url = reverse_lazy('language-list')


class LanguageListView(LoginRequiredMixin, ListView):
    model = Language
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(LanguageListView, self).get_context_data(**kwargs)
        context['language_count'] = Language.objects.all().count()
        return context


class LanguageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'HRQuestions.update_language'
    model = Language
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('language-list')


class LanguageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'HRQuestions.delete_language'
    model = Language
    success_url = reverse_lazy('language-list')


class QuestionListCreateView(LoginRequiredMixin, CreateView):
    template_name = 'questionlist_create.html'
    # model = QuestionList
    form_class = QuestionListModelForm
    success_url = reverse_lazy('question-list-list')


class QuestionListListView(LoginRequiredMixin, ListView):
    model = QuestionList
    template_name = 'questionlist_list.html'
    context_object_name = 'questionlist'
    paginate_by = 5
    queryset = QuestionList.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionListListView, self).get_context_data(**kwargs)
        context['questionlist_count'] = QuestionList.objects.all().count()
        return context


class QuestionFilterView(FilterView):
    filterset_class = QuestionFilter
    template_name = 'search/question_list.html'


class QuestionListDetailView(DetailView):
    model = QuestionList
    paginate_by = 10


class QuestionDetailView(DetailView):
    model = Question
    paginate_by = 10


class QuestionListUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'HRQuestions.update_questionlist'
    model = QuestionList
    form_class = QuestionUpdateModelForm
    # fields = ['name', 'author', 'questions']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('question-list-list')


class QuestionListDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'HRQuestions.delete_questionlist'
    model = QuestionList
    success_url = reverse_lazy('question-list-list')


class QuestionListFilterView(FilterView):
    filterset_class = QuestionListFilter
    template_name = 'search/questionlist_list.html'


class ResetPasswordView(FormView):
    template_name = 'reset_password.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('login-list')

    def form_valid(self, form):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)
        user.set_password(form.cleaned_data["password"])
        user.save()

        return super(ResetPasswordView, self).form_valid(form)


