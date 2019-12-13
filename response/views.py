from django.http import Http404
from django.shortcuts import redirect

from assessment.models import Question, Choice
from response.models import UserResponse, Response


def submit_response(request):
    if request.method == "POST":
        data = request.POST
        user_response = UserResponse(email=data["email"], comments=data["comments"])
        for key, value in data.items():
            try:
                answer = Response(
                    question=Question.objects.get(pk=int(key)),
                    answer=Choice.objects.get(pk=int(value))
                )
                answer.save()
                user_response.answers.add(answer)
            except ValueError as e:
                print(e)

        user_response.save()
        return redirect("/")
    raise Http404("Wrong Entry")
