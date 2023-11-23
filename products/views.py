from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from products.forms import OrderForm
from products.models import Item, Order
from products.services import get_payment, get_basket_payment


# Create your views here.


class ItemDetailView(DetailView):
    model = Item


def page_with_pay_link(request, pk):

    item = get_object_or_404(Item, pk=pk)

    session = get_payment(item)
    context = {"payment_link": session.url}  # Ссылка на стр оплаты

    return render(request, 'products/page_with_link.html', context)


def success_page(request, pk):

    item = get_object_or_404(Item, pk=pk)
    context = {"item": item.name}

    return render(request, 'products/success_page.html', context)


def orders_create(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)  # форма для создания корзины
        order = form.save()
        return redirect(f'/basket/{order.id}')  # при успешном создании отправляет на стр со ссылкой на оплату
    else:
        form = OrderForm()

    return render(request, 'products/basket.html', {'form': form})


def basket_pay_link(request, pk):

    order = get_object_or_404(Order, pk=pk)

    session = get_basket_payment(order)
    context = {"payment_link": session.url}  # Ссылка на стр оплаты

    return render(request, 'products/page_with_link.html', context)


def basket_success_page(request):

    context = {"item": 'собранной корзины'}  # тут важно передать контекст: success_page.html используется и для item
    return render(request, 'products/success_page.html', context)
