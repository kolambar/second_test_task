import os

from config.settings import stripe
from products.models import Item, Order


def get_payment(item: Item):
    """
    Функция делает все необходимое для создания сессии оплаты товара
    :param item:
    :return session:
    """
    product = stripe.Product.create(name=item.name)  # Создается объект класса Product

    # Создается объект цены
    price = stripe.Price.create(
      unit_amount=item.price * 100,  # цену нужно умножать на 100 т.к. иначе будут копейки/центы
      currency=item.currency,  # валюта
      product=product.id,
    )

    # Создается объект Session с ценой
    session = stripe.checkout.Session.create(
      success_url=f"{os.getenv('BASE_URL')}/success/{item.pk}",  # Ссылка при успешном платеже
      line_items=[
        {
          "price": price.id,
          "quantity": 1,
        },
      ],
      mode="payment",
    )

    return session


def get_basket_payment(order: Order):
    """
    Функция делает все необходимое для создания сессии оплаты корзины
    :param order:
    :return session:
    """
    list_items = order.items.all()  # получает в список все товары из корзины
    product = stripe.Product.create(name='Корзина')  # Создается объект класса Product с названием 'Корзина'

    price_list = []  # Создается список для объектов Price
    for item in list_items:
        # Создается объект цены
        price = stripe.Price.create(
            unit_amount=item.price * 100,  # цену нужно умножать на 100 т.к. иначе будут копейки/центы
            currency=item.currency,  # валюта
            product=product.id,
        )
        price_list.append(price)

    line_items = [{"price": price.id, "quantity": 1} for price in price_list]  # Список словарей для создания сессии
    session = stripe.checkout.Session.create(
        success_url=f"{os.getenv('BASE_URL')}/basket_success",  # Ссылка при успешном платеже
        line_items=line_items,
        mode="payment",
    )

    return session
