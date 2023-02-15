from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.http import HttpResponse


# Create your models here.
def validated(value):
    if value == '':
        raise ValidationError(" поле не должно быть пустым")


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    telegram_link = models.CharField(max_length=50, verbose_name="профиль в телеграм", unique=True)
    print(first_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def clean(self):
    #     if len(self.first_name) < 3:
    #         raise ValidationError


class Report(models.Model):
    theme = models.CharField(max_length=250)
    description = models.TextField()
    conclusion = models.TextField()
    what_learned = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(Profile, related_name="reports", through="Language")

    def __str__(self):
        return f'{self.theme}'


class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='languages')
    programming_language = models.CharField(max_length=50, verbose_name='язык программирования')
