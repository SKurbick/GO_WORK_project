from django.db import models


# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Report(models.Model):
    theme = models.CharField(max_length=250)
    description = models.TextField()
    conclusion = models.TextField()
    what_learned = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ManyToManyField(Profile, related_name="reports", through="Language")

    def __str__(self):
        return f'{self.theme}'


class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='languages')
    programming_language = models.CharField(max_length=50, verbose_name='язык программирования')
