from django.shortcuts import render

from assessment.models import Question, Choice


def assessment_page(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    context = {
        "questions": questions,
        "choices": choices
    }

    if request.method == "GET":
        return render(request, "dass21.html", context)
