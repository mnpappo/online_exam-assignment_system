from django.db import models
from quiz.models import CustomUser
from django.utils.timezone import now


# Create your models here.
class PublishAssignment(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assignment_name = models.CharField(help_text="Enter your assignment name", max_length=200)
    ulpoaded_pdf_file = models.FileField(upload_to='teacher_uploads')
    due_date = models.DateTimeField(help_text="What is the last date time for this assignment submission?", default=now)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.assignment_name


class SubmitAssignment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assignment = models.ForeignKey(PublishAssignment, on_delete=models.CASCADE)
    submitted_pdf_file = models.FileField(upload_to='student_uploads')
    given_mark = models.FloatField(help_text="Mark this assignment", default=0.0)
    submission_date_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.assignment.assignment_name

