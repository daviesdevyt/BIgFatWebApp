from . import views
from django.urls import path

urlpatterns = [
    path('transactions/', views.wallet, name='wallet'),
    path("verify/", views.verify_tx),
]