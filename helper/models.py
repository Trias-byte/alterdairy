from django.db import models

# Create your models here.
subjects = {('math', 'математика'), ('english', 'английский'), ('russian', 'русский'), ('chemistry', 'химия'),
            ('physics', 'физика'),  ('french', 'французский'),('german', 'немецкий'), ('japanese', 'японский'),
            ('italian', 'итальянский'), ('informatics', 'информатика'), ('technology', 'технология'),
            ('music', 'музыка'), ('literature', 'литература'), ('art', 'искуство'),
            ('physical education', 'физкультура'), ('Fundamentals of Life Safety', 'ОБЖ'), ('geography', 'география'),
            ('drawing', 'Черчение'), ('social studies', 'Обществознание'), ('biology', 'биология')}


class RequestsHelp(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(choices=subjects, max_length=50)
    classes = models.CharField(max_length=50)
    testQuestion = models.TextField(max_length=1000)

    class Meta:
        ordering = ('classes',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def str(self):
        return self.title