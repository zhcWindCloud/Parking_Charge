from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.contrib.auth import authenticate, login
from . import forms
import datetime


# 管理员登陆ajax验证
@csrf_exempt
@require_POST
def admin_login(request):
    login_form = forms.LoginForm(request.POST)
    username = request.POST.get("username")
    psd = request.POST.get("psd")
    if login_form.is_valid():
        cd = login_form.cleaned_data
        user = authenticate(username=cd.get("username"), password=cd.get("psd"))
        if user:
            login(request, user)
            return HttpResponse("1")

        else:
            return HttpResponse("0")
    print(username, psd)
    print(request.POST)
    print(login_form)


# 记录删除ajax
@csrf_exempt
@require_POST
def usualdelete(request):
    user_ID = request.POST.getlist("ID")
    print(user_ID, str(user_ID), type(user_ID))
    for x in user_ID:
        try:
            models.User_Info.objects.filter(id=x).delete()
            return HttpResponse("1")
        except:
            return HttpResponse("2")


# 会员删除ajax验证
@csrf_exempt
@require_POST
def VIPdelete(request):
    user_ID = request.POST.getlist("ID")
    print("会员删除", user_ID, str(user_ID), type(user_ID))
    for x in user_ID:
        try:
            models.VIPuserInfo.objects.filter(id=x).delete()
            return HttpResponse("1")
        except:
            return HttpResponse("2")


# 会员修改 ajax验证
@csrf_exempt
@require_POST
def VIPedit(request):
    id = request.POST.get("id")
    userid = request.POST.get('userid')
    print(" 会员修改 ajax验证:", id, userid)
    try:
        obj = models.VIPuserInfo.objects.get(id=userid)
        print(obj, type(obj))
        obj.user_ID = id
        obj.save()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


# 会员注册ajax验证
@csrf_exempt
def VIPregister(request):
    if request.method == "POST":
        user_ID = request.POST.get("user_ID")
        phone = request.POST.get("telephone")
        print("会员注册ajax验证:", user_ID, phone)
        if user_ID != '' and phone == None:
            user_object = models.VIPuserInfo.objects.filter(user_ID=user_ID)
            if user_object:
                return HttpResponse("0")
            else:
                return HttpResponse("1")
        elif user_ID == None and phone != '':
            user_object = models.VIPuserInfo.objects.filter(user_phone=phone)
            if user_object:
                return HttpResponse("0")
            else:
                return HttpResponse("1")


# 往来记录添加
@csrf_exempt
@require_POST
def usual_add(request):
    number = request.POST.get("user_number")
    strat = request.POST.get('user_start')
    VIP = request.POST.get('user_VIP')
    try:
        models.User_Info.objects.create(user_ID=number, user_starttime=strat, user_choise=VIP)
        return HttpResponse("1")
    except:
        return HttpResponse("2")


# 往来记录更新
@csrf_exempt
@require_POST
def usual_update(request):
    end = request.POST.get("user_end")
    idd = request.POST.get("userid")
    number = request.POST.get("number")
    # print("# 往来记录更新",number)
    endtime = datetime.datetime.strptime(str(end), "%Y-%m-%d %H:%M:%S")
    try:
        object = models.User_Info.objects.get(id=idd)
        object.user_endtime = endtime
        object.save()
        # print("对象",object.user_choise)
        try:
            starttime = object.user_starttime
            object_days = int((endtime - starttime).days)
            object_seconds = int((endtime - starttime).seconds) + object_days * 3600 * 24
            hours = int(object_seconds / 3600)
            if str(object.user_choise) == "0":
                if hours <= 1:
                    free =10
                else:
                    free = hours * 10
            elif str(object.user_choise) == "1":
                if hours <= 1:
                    free = 8
                else:
                    free = hours * 8
            # print(idd,'记录车费更新',free,object,type(object))
            models.user_charge(user_id = object, user_free=free).save()
            return HttpResponse("1")
        except:
            object.user_endtime = None
            object.save()
            models.user_charge.objects.filter(user_id=number).delete()
            # print("更新", "*" * 78)
            return  HttpResponse("2")
    except:
        # object.user_endtime = None
        # object.save()
        # print("nih")
        return HttpResponse("2")


# 收费ajax 更新收费时间
@csrf_exempt
@require_POST
def free_update(request):
    idd = request.POST.get("ID")
    print(idd)
    try:
        obj = models.user_charge.objects.get(id=idd)
        obj.end_free_time = datetime.datetime.now()
        obj.save()
        return HttpResponse("1")
    except:
        return HttpResponse("2")
