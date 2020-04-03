import datetime

from django.db.models import QuerySet, Max
from django.shortcuts import render
from manager.models import ParkState, ParkSpot, VipCar
from message.models import ParkNow, ParkHis, ErrorMess

# from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required
# 这里需要传输数据库中车库的信息
filters = {
    "0": "A",
    "1": "B",
    "2": "C",
    "3": "D"
}
filters2 = {
    "0": "积水",
    "1": "地面凹陷",
    "2": "施工中",
    "3": "有玻璃残渣"
}


def index(request):
    park_state = ParkState.objects.all()
    # park_now = ParkNow.objects.all()
    # park_total = park_state | park_now
    # print(park_total)
    # park_total = []
    # for state in park_state:
    #     car_id = state.park.parks
    #     park_total.append(state|car_id)
    park_num = park_state.count()
    # park_spot = ParkSpot.objects.all()
    # park_now = park_spot.first().parks

    context = {
        "park_state": park_state,
        "park_num": park_num,
        # "park_now": park_now
    }
    return render(request, 'manager/index.html', context)


def car1(request):
    # park_now = ParkNow.objects.all()
    if request.method == "POST":
        if request.POST.get("sig") == "提交":
            flag = ParkNow.objects.filter(car_id=request.POST.get("car_id")).exists()
            if flag:
                park_now = ParkNow.objects.get(car_id=request.POST.get("car_id"))
                state = ParkState.objects.filter(
                    park=park_now.park).update(state=0)
                car_id = park_now.car_id
                begin_time = park_now.begin_time
                money = 12.0
                park = park_now.park
                park_his = ParkHis(car_id=car_id, begin_time=begin_time, money=money, park=park)
                park_his.save()
                park_now.delete()
                return render(request, 'car_3.html', {"car_id": request.POST.get("car_id")})
            else:
                return render(request, 'car_2.html', {"car_id": request.POST.get("car_id")})
        else:
            vip_car_id = request.POST.get("car_id")
            max_id = VipCar.objects.all().aggregate(Max('vip'))["vip__max"]
            vip_code = str(int(max_id) + 1)
            vip = VipCar(car_id=vip_car_id, vip=vip_code)
            vip.save()
            return render(request, 'car_1.html')

    else:
        return render(request, 'car_1.html')


def car2(request):
    if request.method == "POST":
        car_id = request.POST.get("car_id")
        area = request.POST.get("dropdown")
        spot_num = request.POST.get("spot_num")
        park = ParkSpot.objects.filter(area=area, spot_num=spot_num).first()
        print(park)
        now = ParkNow(car_id=car_id, park=park)
        now.save()
        state = ParkState.objects.filter(park=park).update(state=1)
        return render(request, 'car_1.html')

    return render(request, 'car_2.html')


def car3(request):
    return render(request, 'car_3.html')


def spot1(request):
    if request.method == "POST":
        if request.POST.get("sip") == "提交":
            park = ParkSpot.objects.filter(area=request.POST.get("dropdown"),
                                           spot_num=request.POST.get("spot_num")).first()
            area = filters[request.POST.get("dropdown")]
            spot_num = request.POST.get("spot_num")
            park_state = ParkState.objects.filter(park=park)
            flag = ErrorMess.objects.filter(park=park).exists()

            if flag:
                error_message = ErrorMess.objects.filter(park=park).values("error_message").first()["error_message"]
                print(error_message)
                return render(request, "spot_3.html",
                              {"area": area, "spot_num": spot_num, "error_message": error_message})
            else:
                park_id = ParkSpot.objects.filter(area=request.POST.get("dropdown"),
                                                  spot_num=request.POST.get("spot_num")).values("id").first()["id"]
                print(park_id)
                return render(request, 'spot_2.html', {"park_id": park_id})

    return render(request, 'spot_1.html')


def spot2(request):
    if request.method == "POST":
        park = ParkSpot.objects.filter(id=request.POST.get("car_id")).first()
        print(park)
        error_message = filters2[request.POST.get("dropdown2")]
        error = ErrorMess(park=park, error_message=error_message)
        error.save()
        state = ParkState.objects.filter(park=park).update(state=2)
        return render(request, 'spot_1.html')
    return render(request, 'spot_1.html')


def spot3(request):
    return render(request, 'spot_1.html')

# def in_or_out(request):
#     if request.method == "POST":
#         flag = ParkNow.objects.filter(car_id=request.POST.get("car_id")).exists()
#         if flag:
#             print("hhhhh")
#             return render(request, 'car_3.html')
#         else:
#             print("www")
#             return render(request, 'car_2.html')
