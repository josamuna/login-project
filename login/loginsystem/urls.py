from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.getLogins),
    path('signup/', views.addUser),
    path('<int:pk>/', views.login_detail),
]