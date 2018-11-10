from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Quiz, Question, Choice, QuizResult, CustomUser
import datetime



def index(request):
    quiz = Quiz.objects.all()
    template = loader.get_template('index.html')

    context = {
        'quiz': quiz,
    }
    return HttpResponse(template.render(context, request))


@login_required
def quiz_page(request, quiz_id):
    template = loader.get_template('quiz.html')
    uid = request.user.id

    quiz = Quiz.objects.get(pk=quiz_id)
    questions = quiz.question_set.all()

    try:
        result = QuizResult.objects.filter(student=uid, quiz=quiz)
        rlen = len(result)
        result = result[0]
    except IndexError as e:
        print (e)
        pass

    context = {
        'qz': quiz,
        'questions': questions,
        'result': result,
        'rlen': rlen
    }
    return HttpResponse(template.render(context, request))


def quiz_action(request):
    user_id = request.POST['static_user_id']
    quiz_id = request.POST['form_quiz_id']
    return redirect('/quiz_page/' + str(quiz_id))


def result_processing(request, quiz_id):
    qid = quiz_id
    uid = request.user.id

    qi = Quiz.objects.get(pk=quiz_id)
    si = CustomUser.objects.get(pk=uid)

    count = QuizResult.objects.filter(student=si, quiz=qi).count()
    if count > 0:
        pass
    else:
        t = request.POST.getlist('question_x')
        quiz = Quiz.objects.get(pk=quiz_id)
        questions = quiz.question_set.all()
        correct_answers = []
        for q in questions:
            cs = q.choice_set.all()
            for c in cs:
                if c.is_correct:
                    correct_answers.append(c.id)
        
        sub_ans = [int(x) for x in t]
        
        c = [i for i in correct_answers if i in sub_ans]
        obtained_mark = len(c)
        
        r = QuizResult(quiz=qi, student=si, mark=obtained_mark)
        r.save()

    return redirect('/quiz_page/' + str(quiz_id))