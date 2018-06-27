from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    # у сообщения должны быть автор, время, текст
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):  # переопределение метода ->
        #  вместо счетчика сообщений его содержимое
        return self.text

