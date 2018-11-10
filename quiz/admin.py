from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Quiz, Question, Choice, CustomUser, QuizResult

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id','email', 'username', 'student_id', 'department']


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz_name', 'pub_date_time', 'created_at', 'duration')

admin.site.register(Quiz, QuizAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['quiz_name_id', 'student_name_id', 'mark']
    list_filter = ('quiz', 'student')
    search_fields = ['quiz', 'student']


    def quiz_name_id(self, obj):
        return '{quiz_name} - {quiz_id}'.format(quiz_name = obj.quiz.quiz_name, quiz_id = obj.quiz.id)
    quiz_name_id.short_description = 'Quiz name-id'
    quiz_name_id.allow_tags = True

    def student_name_id(self, obj):
        return '{student} - {student_f_name} {student_l_name}'.format(student = obj.student.id, student_f_name=obj.student.first_name, student_l_name=obj.student.last_name)
    student_name_id.short_description = 'Student Id'
    student_name_id.allow_tags = True

    

admin.site.register(Question, QuestionAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(QuizResult, QuizResultAdmin)


admin.site.site_header = "OES Dashboard"
admin.site.site_title = "Online Examination System"
admin.site.index_title = "Welcome to OES"
