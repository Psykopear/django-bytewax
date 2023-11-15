import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangowax.settings")

import django

django.setup()

from wax.models import Question

from bytewax.dataflow import Dataflow
from bytewax.testing import TestingInput
from bytewax.connectors.stdio import StdOutput


def format_questions(q__choices):
    q, choices = q__choices
    choices = "\n".join(f"- {c}" for c in choices)
    return f"{q}:\n{choices}"


flow = Dataflow()
flow.input("in", TestingInput(Question.objects.all()))
flow.map(
    lambda q: (q.question_text, q.choice_set.values_list("choice_text", flat=True))
)
flow.map(format_questions)
flow.output("out", StdOutput())
