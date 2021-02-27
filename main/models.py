from django.db import models

# Create your models here.


class Peaples(models.Model):
    firstName = models.CharField('Фамилия', max_length=25)
    secondName = models.CharField('Имя', max_length=25)
    thirdName = models.CharField('Очество', max_length=25)
    school = models.CharField('Школа', max_length=25)
    rayon = models.CharField('Район', max_length=25)
    login = models.CharField('логин', max_length=25)
    role = models.CharField('Ученик/Учитель', max_length=10)
    password = models.CharField('пароль', max_length=10)
    classes = models.CharField('Класс ', blank=True, max_length=2)
    passwordParents = models.CharField('Пароль для родителей', blank=True, max_length=10)

    class Meta:
        ordering = ('login',)
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def str(self):
        return self.firstName


class CsvReader(models.Model):
    upload = models.FileField(upload_to='uploads/')