from django.db import models


class Question(models.Model):
    english_text = models.CharField(max_length=200, verbose_name="Question(English)")
    hindi_text = models.CharField(max_length=200, verbose_name="Question(Hindi)")

    def __str__(self):
        return self.english_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text
