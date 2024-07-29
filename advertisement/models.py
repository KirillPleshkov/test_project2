from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='заголовок')
    author = models.CharField(max_length=200, verbose_name='автор')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    position = models.PositiveIntegerField(verbose_name='позиция')

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'

    def __str__(self):
        return self.title
