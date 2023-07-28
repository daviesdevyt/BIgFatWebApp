from . import views
from django.urls import path

urlpatterns = [
    path('news/', views.news, name='news'),
]