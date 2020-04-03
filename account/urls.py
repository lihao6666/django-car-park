from django.urls import path

from . import views
app_name = "account"
urlpatterns = [
    path('login', views.acc_login, name="login"),
]
