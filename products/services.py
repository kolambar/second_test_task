from config.settings import stripe


def get_payment(item):
    product = stripe.Product.create(name=item.name)

    price = stripe.Price.create(
      unit_amount=item.price * 100,
      currency=item.currency,
      product=product.id,
    )

    session = stripe.checkout.Session.create(
      success_url=f"http://127.0.0.1:8000/success/{item.pk}",
      line_items=[
        {
          "price": price.id,
          "quantity": 1,
        },
      ],
      mode="payment",
    )

    return session
