from products.apps import ProductsConfig
from django.urls import path

from products.views import ItemDetailView

app_name = ProductsConfig.name


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='detail'),
]