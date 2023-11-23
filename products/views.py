from django.shortcuts import render
from django.views.generic import DetailView

from products.models import Item


# Create your views here.


class ItemDetailView(DetailView):
    model = Item
