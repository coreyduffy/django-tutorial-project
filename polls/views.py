from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Question


# Create your views here.
def index(request):
    questions = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in questions])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(get_object_or_404(Question, pk=question_id))


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
