import requests
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render

from assessment.models import Question, Choice
from response.models import UserResponse, Response
from src import settings


def submit_response(request):
    if request.method == "POST":

        recaptcha_response = request.POST.get('g-recaptcha-response')

        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            data = request.POST
            user_response = UserResponse(email=data["email"], comments=data["comments"])
            user_response.save()
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
            try:
                send_mail(
                    'Thank you for taking out the time',
                    'Your Assessment id is ' + user_response.response_id,
                    'madhavpruthi0@gmail.com',
                    [user_response.email],
                    fail_silently=False,
                )
            except Exception as e:
                print("Exception Occured: " + str(e))
            return render(request, "thank-you.html", {"assessment_id": user_response.response_id})
        else:
            raise Http404("ReCaptcha Not Verified")
    raise Http404("Wrong Entry")
