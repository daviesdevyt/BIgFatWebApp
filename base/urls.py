from . import views
from django.urls import path

urlpatterns = [
    path('news/', views.news, name='news'),
    path('transactions/', views.wallet, name='wallet'),
    path('support/', views.support, name='support'),
]