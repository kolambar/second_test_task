import os

from config.settings import stripe


def get_payment(item):
    product = stripe.Product.create(name=item.name)

    price = stripe.Price.create(
      unit_amount=item.price * 100,
      currency=item.currency,
      product=product.id,
    )

    session = stripe.checkout.Session.create(
      success_url=f"{os.getenv('BASE_URL')}/success/{item.pk}",
      line_items=[
        {
          "price": price.id,
          "quantity": 1,
        },
      ],
      mode="payment",
    )

    return session


def get_basket_payment(order):
    list_items = order.items.all()

    product = stripe.Product.create(name='Корзина')
    price_list = []
    for item in list_items:
        price = stripe.Price.create(
            unit_amount=item.price * 100,
            currency=item.currency,
            product=product.id,
        )
        price_list.append(price)

    line_items = [
        {"price": price.id, "quantity": 1} for price in price_list
    ]

    session = stripe.checkout.Session.create(
        success_url=f"{os.getenv('BASE_URL')}/basket_success/{order.pk}",

        line_items=line_items,
        mode="payment",
    )

    return session
