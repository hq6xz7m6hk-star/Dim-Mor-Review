from django.db import models

# Create your models here.
class Review(models.Model):

        name = models.CharField(max_length=40, verbose_name='ФИО', blank=False)
        email = models.EmailField(verbose_name='Email')
        text = models.TextField(verbose_name='Текст отзыва')
        checked = models.BooleanField(default=False, verbose_name='Проверено')


        def __str__(self):
            return f'{self.name} ({self.email})'