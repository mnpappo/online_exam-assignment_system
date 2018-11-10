from django.apps import AppConfig


class QuizConfig(AppConfig):
    name = 'quiz'


from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
