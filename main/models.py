from django.db import models

# Create your models here.


class Peaple(models.Model):
    firstName = models.CharField('Фамилия', max_length=25)
    secondName = models.CharField('Имя', max_length=25)
    thirdName = models.CharField('Очество', max_length=25)
    school = models.CharField('Школа', max_length=25)
    rayon = models.CharField('Район', max_length=25)
    login = models.CharField('логин', max_length=25)
    role = models.CharField('Ученик/Учитель', max_length=10)
    password = models.CharField('пароль', max_length=10)
    classes = models.CharField('Класс (None в случе отсутствия)', max_length=25)
    passwordParents = models.CharField('Пароль для родителей (None в случе ненадобности)', max_length=10)

    class Meta:
        ordering = ('login',)
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def str(self):
        return self.firstName
