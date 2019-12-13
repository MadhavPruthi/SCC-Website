from django.db import models
from django.utils.crypto import get_random_string

from assessment.models import Question, Choice


def generate_random_string():
    return get_random_string(12,
                             allowed_chars='abcdefghijklmnopqrstuvwxyz''ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.question.id) + " - " + str(self.answer.id)


class UserResponse(models.Model):
    response_id = models.CharField(primary_key=True, default=generate_random_string, editable=False, max_length=12)
    email = models.EmailField()
    dateTime = models.DateTimeField(auto_now=True)
    answers = models.ManyToManyField(Response)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.response_id) + " - " + self.email
