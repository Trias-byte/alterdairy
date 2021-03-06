# Generated by Django 3.1.7 on 2021-02-25 21:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestsHelps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subject', models.CharField(choices=[('Музыка', 'Музыка'), ('Итальянский', 'Итальянский'), ('Обществознание', 'Обществознание'), ('Алгебра', 'Алгебра'), ('Физкультура', 'Физкультура'), ('Геометрия', 'Геометрия'), ('Французский', 'Французский'), ('География', 'География'), ('Черчение', 'Черчение'), ('Искуство', 'Искуство'), ('Литература', 'Литература'), ('Право', 'Право'), ('Русский', 'Русский'), ('Психология', 'Психология'), ('Химия', 'Химия'), ('Математика', 'Математика'), ('Биология', 'Биология'), ('Астрономия', 'Астрономия'), ('Английский', 'Английский'), ('Окружающий мир', 'Окружающий мир'), ('Японский', 'Японский'), ('Физика', 'Физика'), ('Информатика', 'Информатика'), ('Технология', 'Технология'), ('ОБЖ', 'ОБЖ'), ('Экономика', 'Экономика'), ('Немецкий', 'Немецкий')], max_length=50)),
                ('bals', models.IntegerField()),
                ('classes', models.CharField(max_length=50)),
                ('testQuestion', models.TextField(max_length=1000)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('classes',),
            },
        ),
        migrations.DeleteModel(
            name='RequestsHelp',
        ),
    ]
