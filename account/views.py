from django.shortcuts import render, redirect
from account import models
# Create your views here.
from django.http import HttpResponse


def acc_login(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    elif request.method == 'POST':
        pwd = models.Admin.objects.filter(account=request.POST.get('account')).values("password").first()["password"]
        if pwd == request.POST.get('password'):
            return redirect(request.GET.get('next', '/manager'))
        else:
            return render(request, 'account/logœin.html', {'erro': "用户名或密码错误"})

