from django.db import models

# Create your models here.


class Peaple (models):
    firstName = models.CharField('Имя', max_length=25)
    secondName = models.CharField('Имя', max_length=25)
    thirdName = models.CharField('Имя', max_length=25)
    classes = models.CharField('Имя', max_length=25)
    school = models.CharField('Имя', max_length=25)
    rayon = models.CharField('Имя', max_length=25)
    login = models.CharField('Имя', max_length=25)
    role = models.CharField('Имя', max_length=10)
    password = models.CharField('Имя', max_length=10)
    if role == 'ученик':
        passwordParents = models.CharField('Имя', max_length=10)

    class Meta:
        ordering = ('login',)
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def str(self):
        return self.title
