from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from  . import models
import  datetime
import django
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from . import  forloop1
# Create your views here.


# //管理员登录

@csrf_exempt
def mylogin(request):
    if request.method == "GET":
        return render(request, "Login.html")
    elif request.method == "POST":
        return HttpResponse("1")


# 会员注册
@csrf_exempt
@login_required()
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        user_ID = request.POST.get("user_number")
        user_name = request.POST.get("user_name")
        user_phone = request.POST.get("user_phone")
        user_birth =request.POST.get("user_birth")
        user_sex = request.POST.get("user_sex")
        birth_day = int(user_birth[0:4])
        now_year = int(datetime.datetime.now().year)
        grade = str(now_year - birth_day)
        print(user_ID, user_name, user_phone, user_birth, user_sex)
        if user_sex == None:
            return  HttpResponse("0")
        else:
            models.VIPuserInfo.objects.create(user_ID=user_ID,user_nanme=user_name,user_phone=user_phone
                                          ,user_birth=user_birth,user_sex=user_sex,user_grade=grade)

        return HttpResponse("1")








# 后台主页
@csrf_exempt
@login_required()
def index(request):
    print(django.get_version())
    return render(request, "index.html")


@csrf_exempt
@login_required()
def usual(request):
    return render(request, "usual.html",{'user_type':"usual"})


@csrf_exempt
@login_required()
def VIP(request):
    user_type = "VIP"
    return render(request, "usual.html",{'user_type':user_type})



# 查看的 iframe
@csrf_exempt
def vip_detail_iframe(request):
    return render(request,"iframe.html",context= { 'vip_type':"detail"})


# 编辑 的 iframe
def vip_edit_iframe(request):
    return render(request,"iframe.html",context= {'vip_type':"edit"})

#二维码的iframe
def QRcode_iframe(request):
    return render(request,"iframe.html",context= {'free':"free"})

def usual_iframe(request):
    return render(request,"iframe.html",context={"usual":"usual"})


@login_required()
def free(request):
    return render(request,"usual.html",context={"free":"free"})





def forloopd(request):
    forloop1.fo()
    return  HttpResponse("....................")


