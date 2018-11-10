from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return ('{id} - {firstname} {lastname}').format(id = str(self.id), firstname=self.first_name, lastname=self.last_name)


class Quiz(models.Model):
    quiz_name = models.CharField(help_text="Enter your quiz name", max_length=200)
    pub_date_time = models.DateTimeField(help_text="What time do you want to start the quiz?")
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.DecimalField(help_text="The quiz duration(in minutes)", max_digits=4, decimal_places=1, default=30.00)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(help_text="Your question", max_length=200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(help_text="Choice", max_length=200)
    is_correct = models.BooleanField(help_text="Is this choice correct?", default=False)
    def __str__(self):
        return self.choice_text
    

class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()
    def __str__(self):
        return str(self.mark)
