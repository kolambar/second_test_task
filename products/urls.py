from products.apps import ProductsConfig
from django.urls import path

from products.views import ItemDetailView, page_with_pay_link, success_page, orders_create, basket_pay_link, \
    basket_success_page

app_name = ProductsConfig.name


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='detail'),  # Страница просмотра товара
    path('buy/<int:pk>/', page_with_pay_link, name='buy'),  # Страница со ссылкой на оплату
    path('success/<int:pk>/', success_page),  # Страница успешной оплаты товара
    path('basket/', orders_create, name='basket'),  # Страница сбора корзины
    path('basket/<int:pk>/', basket_pay_link, name='buy_basket'),  # Страница со ссылкой на оплату
    path('basket_success/', basket_success_page),  # Страница успешной оплаты корзины
]
