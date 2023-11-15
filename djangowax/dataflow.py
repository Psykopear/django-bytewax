import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangowax.settings")

import django

django.setup()

from wax.models import Question

from bytewax.dataflow import Dataflow
from bytewax.testing import TestingInput
from bytewax.connectors.stdio import StdOutput

flow = Dataflow()
flow.input("in", TestingInput(Question.objects.all()))
flow.output("out", StdOutput())
