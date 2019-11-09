from django.contrib import admin

# Register your models here.

from django.contrib import admin

from HRQuestions.models import Language, Question, QuestionList


# class LanguageAdmin(admin.ModelAdmin):
    # list_display = ['name']

admin.site.register(Language)


# class QuestionAdmin(admin.ModelAdmin):
    # list_display = ['title', 'author']

admin.site.register(Question)


# class QuestionListAdmin(admin.ModelAdmin):
    # list_display = ['name', 'author', 'question']


admin.site.register(QuestionList)

