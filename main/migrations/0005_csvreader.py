# Generated by Django 3.1.7 on 2021-02-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_schools'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvReader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
