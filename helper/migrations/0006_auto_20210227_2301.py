# Generated by Django 3.1.7 on 2021-02-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0005_auto_20210227_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestshelps',
            name='subject',
            field=models.CharField(choices=[('Химия', 'Химия'), ('Немецкий', 'Немецкий'), ('Японский', 'Японский'), ('Информатика', 'Информатика'), ('Обществознание', 'Обществознание'), ('Английский', 'Английский'), ('Музыка', 'Музыка'), ('География', 'География'), ('Астрономия', 'Астрономия'), ('Психология', 'Психология'), ('Физкультура', 'Физкультура'), ('Экономика', 'Экономика'), ('Итальянский', 'Итальянский'), ('Физика', 'Физика'), ('Биология', 'Биология'), ('Геометрия', 'Геометрия'), ('Право', 'Право'), ('Математика', 'Математика'), ('ОБЖ', 'ОБЖ'), ('Окружающий мир', 'Окружающий мир'), ('Алгебра', 'Алгебра'), ('Черчение', 'Черчение'), ('Французский', 'Французский'), ('Технология', 'Технология'), ('Искуство', 'Искуство'), ('Русский', 'Русский'), ('Литература', 'Литература')], max_length=50),
        ),
    ]
