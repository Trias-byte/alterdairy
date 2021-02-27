from django.db import models
from django.utils import timezone
# Create your models here.
subjects = {('Математика', 'Математика'), ('Английский', 'Английский'), ('Русский', 'Русский'), ('Химия', 'Химия'),
            ('Физика', 'Физика'),  ('Французский', 'Французский'), ('Немецкий', 'Немецкий'), ('Японский', 'Японский'),
            ('Итальянский', 'Итальянский'), ('Информатика', 'Информатика'), ('Технология', 'Технология'),
            ('Музыка', 'Музыка'), ('Литература', 'Литература'), ('Искуство', 'Искуство'),
            ('Физкультура', 'Физкультура'), ('ОБЖ', 'ОБЖ'), ('География', 'География'),
            ('Черчение', 'Черчение'), ('Обществознание', 'Обществознание'), ('Биология', 'Биология'),
            ('Алгебра', 'Алгебра'), ('Геометрия', 'Геометрия'), ('Право', 'Право'),
            ('Окружающий мир', 'Окружающий мир'), ('Экономика', 'Экономика'), ('Астрономия', 'Астрономия'),
            ('Психология', 'Психология'), }


class RequestsHelps(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(choices=subjects, max_length=50)
    bals = models.IntegerField()
    classes = models.CharField(max_length=50)
    testQuestion = models.TextField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('classes',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def str(self):
        return self.title