# Generated by Django 2.2.10 on 2021-11-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Иванов Иван Иванович', max_length=255)),
                ('email', models.EmailField(default='email@mail.com', max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
