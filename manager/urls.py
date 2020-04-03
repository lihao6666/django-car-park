from django.urls import path

from . import views

app_name = "manager"
urlpatterns = [
    path('', views.index, name="index"),
    path('car1', views.car1, name="car1"),
    path('car2', views.car2, name="car2"),
    path('car3', views.car3, name="car3"),

    path('spot1', views.spot1, name="spot1"),
    path('spot2', views.spot2, name="spot2"),
    path('spot3', views.spot3, name="spot3"),


]
