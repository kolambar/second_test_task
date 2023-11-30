from django.db import models

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):

    CUR = (
        ('USD', 'доллары'),
        ('RUB', 'рубли'),
    )  # тут можно добавить валюту

    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    currency = models.CharField(max_length=10, verbose_name='способ оплаты', choices=CUR)  # валюты две. добавить можно в CUR

    def __str__(self):
        return f'{self.name} - {self.price}{self.currency}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):  # С помощью корзины можно покупать сразу несколько товаров
    items = models.ManyToManyField(Item, verbose_name='Товары')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return ', '.join(str(item) for item in self.items.all())
