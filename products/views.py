from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.response import Response

from products.models import Item
from products.services import get_payment


# Create your views here.


class ItemDetailView(DetailView):
    model = Item


def page_with_pay_link(request, pk):

    item = Item.objects.get(pk=pk)
    session = get_payment(item)

    context = {"payment_link": session.url}

    return render(request, 'products/page_with_link.html', context)


def success_page(request, pk):

    item = Item.objects.get(pk=pk)
    context = {"item": item.name}

    return render(request, 'products/success_page.html', context)
