from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz_page/<int:quiz_id>', views.quiz_page, name='quiz_page'),
    path('quiz_action/', views.quiz_action, name='quiz_action'),
    path('result_processing/<int:quiz_id>', views.result_processing, name='result_processing')
]