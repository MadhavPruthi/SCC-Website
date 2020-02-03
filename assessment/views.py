from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from assessment.models import Question, Choice
from response.models import UserResponse


def assessment_page(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    context = {
        "questions": questions,
        "choices": choices
    }

    if request.method == "GET":
        return render(request, "public/dass21.html", context)


@login_required()
def check_assessment_view(request):
    return render(request, 'admin/findAssessment.html', {})


@login_required()
def show_particular_assessment(request):
    assessment_id = request.GET.get('assessment_id', '')
    if UserResponse.objects.filter(response_id=assessment_id).exists():
        user_response = UserResponse.objects.get(response_id=assessment_id)
        questions = Question.objects.all()
        choices = Choice.objects.all()
        context = {
            "questions": questions,
            "choices": choices,
            "user_response": user_response,
        }
        return render(request, 'admin/adminDass21.html', context)
    else:
        return render(request, 'admin/findAssessment.html',
                      {"error_message": assessment_id + " doesn't exist in our database!"})
