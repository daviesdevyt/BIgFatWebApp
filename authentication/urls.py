from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("change-password/", views.change_password, name="cart"),
    path("logout/", views.logout, name="logout"),
]