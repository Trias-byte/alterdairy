# Generated by Django 3.1.7 on 2021-02-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peaple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25, verbose_name='Имя')),
                ('secondName', models.CharField(max_length=25, verbose_name='Имя')),
                ('thirdName', models.CharField(max_length=25, verbose_name='Имя')),
                ('classes', models.CharField(max_length=25, verbose_name='Имя')),
                ('school', models.CharField(max_length=25, verbose_name='Имя')),
                ('rayon', models.CharField(max_length=25, verbose_name='Имя')),
                ('login', models.CharField(max_length=25, verbose_name='Имя')),
                ('role', models.CharField(max_length=10, verbose_name='Имя')),
                ('password', models.CharField(max_length=10, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ('login',),
            },
        ),
    ]
