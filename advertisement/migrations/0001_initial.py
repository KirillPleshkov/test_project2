# Generated by Django 4.2.14 on 2024-07-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='заголовок')),
                ('author', models.CharField(max_length=200, verbose_name='автор')),
                ('views_count', models.IntegerField(verbose_name='количество просмотров')),
                ('position', models.IntegerField(verbose_name='позиция')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
            },
        ),
    ]
