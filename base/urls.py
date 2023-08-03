from . import views
from django.urls import path

urlpatterns = [
    path('', views.news, name='news'),
    path('news/', views.news, name='news'),
    path('transactions/', views.wallet, name='wallet'),
    path('support/', views.support, name='support'),
    path('cc/', views.cc, name='cc'),
    path('fullz/', views.fullz, name='fullz'),
    path('dumps/', views.dumps, name='dumps'),
    path("cart/", views.cart, name="cart"),
    path("purchases/", views.purchases, name="purchases"),
    path("verify/", views.verify_tx),
    path("empty-cart/", views.empty_cart, name="empty-cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("delete-cart/<str:prod_id>", views.delete_cart, name="del-cart"),
    path("add-cart/<str:type>/<str:prod_id>", views.add_cart, name="add-cart"),
    path('<str:title>/', views.logs, name='logs'),
]