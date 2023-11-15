from django.core.management.base import BaseCommand
from django.utils import timezone
from wax.models import Question, Choice


class Command(BaseCommand):
    help = "Load some test data"

    def handle(self, *args, **kwargs):
        name = Question.objects.create(
            question_text="What's your name?", pub_date=timezone.now()
        )
        Choice.objects.create(question=name, choice_text="John")
        Choice.objects.create(question=name, choice_text="Paul")
        Choice.objects.create(question=name, choice_text="Jhon")
        age = Question.objects.create(
            question_text="What's your age?", pub_date=timezone.now()
        )
        Choice.objects.create(question=age, choice_text="42")
        Choice.objects.create(question=age, choice_text="43")
        Choice.objects.create(question=age, choice_text="44")
