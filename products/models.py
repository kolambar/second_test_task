from django.db import models

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    CUR = (
        ('USD', 'доллары'),
        ('RUB', 'рубли'),
    )
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    currency = models.CharField(max_length=10, verbose_name='способ оплаты', choices=CUR)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
