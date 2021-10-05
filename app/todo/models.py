from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Задача')
    complete = models.BooleanField(default=False, verbose_name='Завершено?')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Записано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
