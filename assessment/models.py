from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=200, verbose_name="Question")

    def __str__(self):
        return self.question


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text
