from django.shortcuts import render
from message.models import ParkNow, ParkHis, ErrorMess, TipMess
from manager.models import ParkState, ParkSpot, VipCar

filters = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3
}


# Create your views here.
def index(request):
    return render(request, "message/index.html")


def park_now_list(request):
    park_now = ParkNow.objects.all()
    return render(request, "message/park_now_list.html", {"park_now": park_now})


def park_his_list(request):
    if request.method == "POST":
        # print(request.POST.get("delete"))
        delete = ParkHis.objects.filter(car_id=request.POST.get("delete")).delete()

    park_his = ParkHis.objects.all()
    return render(request, "message/park_his_list.html", {"park_his": park_his})


def park_info_list(request):
    park_state = ParkState.objects.all()
    return render(request, "message/park_info_list.html", {"park_state": park_state})


def park_error_list(request):
    if request.method == "POST":
        delete = ErrorMess.objects.filter(park__area=filters[request.POST.get("area_id")],
                                          park__spot_num=request.POST.get("spot_id")).delete()
        state = ParkState.objects.filter(park__area=filters[request.POST.get("area_id")],
                                         park__spot_num=request.POST.get("spot_id")).update(state=0)
        tip_message = request.POST.get("area_id") + "区" + request.POST.get("spot_id") + "号车位已修复"
        tip = TipMess(tip_message=tip_message)
        tip.save()
    park_error = ErrorMess.objects.all()
    print("WWW")
    print(park_error.first())
    return render(request, "message/park_error_list.html", {"park_error": park_error})


def tip_info_list(request):
    tip_info = TipMess.objects.all()
    return render(request, "message/tip_info_list.html", {"tip_info": tip_info})


def vip_car_list(request):
    if request.method == "POST":
        delete = VipCar.objects.filter(car_id=request.POST.get("vip")).delete()
    vip_car = VipCar.objects.all()
    return render(request, "message/vip_car_list.html", {"vip_car": vip_car})
