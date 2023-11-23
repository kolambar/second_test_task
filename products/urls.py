from products.apps import ProductsConfig
from django.urls import path

from products.views import ItemDetailView, page_with_pay_link, success_page

app_name = ProductsConfig.name


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('buy/<int:pk>/', page_with_pay_link, name='buy'),
    path('success/<int:pk>/', success_page),
]
