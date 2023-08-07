from . import views
from django.urls import path

urlpatterns = [
    path('transactions/', views.wallet, name='wallet'),
    path("verify/<str:pay_id>", views.verify_tx),
]