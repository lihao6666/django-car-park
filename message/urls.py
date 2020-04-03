from django.urls import path

from . import views
app_name = "message"

urlpatterns = [
    path('', views.index, name="index"),
    path('park_now_list', views.park_now_list, name="park_now_list"),
    path('park_his_list', views.park_his_list, name="park_his_list"),
    path('park_info_list', views.park_info_list, name="park_info_list"),
    path('park_error_list', views.park_error_list, name="park_error_list"),
    path('tip_info_list', views.tip_info_list, name="tip_info_list"),
    path('vip_car_list', views.vip_car_list, name="vip_car_list"),
]
