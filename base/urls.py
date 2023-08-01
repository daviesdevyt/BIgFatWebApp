from . import views
from django.urls import path

urlpatterns = [
    path('news/', views.news, name='news'),
    path('transactions/', views.wallet, name='wallet'),
    path('support/', views.support, name='support'),
    path('cc/', views.cc, name='cc'),
    path('fullz/', views.fullz, name='fullz'),
    path('dumps/', views.dumps, name='dumps'),
    path('<str:title>/', views.logs, name='logs'),
]