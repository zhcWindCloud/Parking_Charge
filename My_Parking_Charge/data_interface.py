from .models import *
from django.http import JsonResponse, HttpResponse
import  json,datetime,time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #Django 内置分页
# return returnResponse({'code': 400, 'message': '返回信息'})
# {"code":0,"msg":"","count":1000,"data":[{}]}


# 常规用户的记录数据接口
def usual_data_interface(request):
    user_object = User_Info.objects.all()
    id = request.GET.get("id")  # 搜索重载
    order = request.GET.get("order")  # 排序方式 ： asc  desc or null
    field = request.GET.get("field")  # 排序字段

    if field:
        if order == "asc" or order == "":
            user_object = User_Info.objects.all().order_by("user_ID")
        else:
            user_object = User_Info.objects.all().order_by("-user_ID")
    else:
        if id:
            user_object = User_Info.objects.filter(user_ID=id)
        else:
            user_object = User_Info.objects.all()  # 常规展示
    data_list = []
    for i in user_object:
        dict = {}
        start = i.user_starttime.strftime('%Y-%m-%d %H:%M:%S')  # strptime()内参数必须为string格式
        if i.user_endtime == None:
            end = ''
        else:
            end = i.user_endtime.strftime('%Y-%m-%d %H:%M:%S')
        dict["userid"] = i.id
        dict["id"] = i.user_ID
        dict["starttime"] = start
        dict["endtime"] = end
        dict["user_rank"] = i.get_user_choise_display()
        data_list.append(dict)

    page = request.GET.get('page')  # 前端传来的页数
    limit = request.GET.get("limit")  # 前端传来的一页有几条数量

    # 分页
    paginator = Paginator(data_list, limit)
    try:
        current_page = paginator.page(page)  # 分页器进行分配
        articles = current_page.object_list  # 一个列表
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list

    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    data = {"code": 0, "msg": "", "count": user_object.count(), "data": articles}
    return JsonResponse(data, content_type="application/json")



# 会员数据接口
def VIP__data_interface(request):
    id = request.GET.get("test")                  #搜索重载
    order = request.GET.get("order")        #排序方式 ： asc  desc or null
    field =request.GET.get("field")             #排序字段

    if field:
        if order =="asc" or order=="":
            user_object = VIPuserInfo.objects.all().order_by("user_ID")
        else:
            user_object = VIPuserInfo.objects.all().order_by("-user_ID")
    else:
        if id:
            user_object = VIPuserInfo.objects.filter(user_ID=id)
        else:
            user_object = VIPuserInfo.objects.all()             #常规展示
    data_list = []
    for i in user_object:
        dict = {}
        dict["id"] = i.user_ID
        dict["username"] = i.user_nanme
        dict["sex"] = i.user_sex
        dict["user_rank"] = i.uer_rank
        dict["grade"] = i.user_grade
        dict["birth"] = i.user_birth
        dict["phone"] = i.user_phone
        dict["userid"] = i.id
        data_list.append(dict)

    page = request.GET.get('page')  # 前端传来的页数
    limit = request.GET.get("limit")  # 前端传来的一页有几条数量

    # 分页
    paginator = Paginator(data_list, limit)
    try:
        current_page = paginator.page(page)  # 分页器进行分配
        articles = current_page.object_list  # 一个列表
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list

    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    data = {"code": 0, "msg": "", "count": user_object.count(), "data": articles}
    return JsonResponse(data, content_type="application/json")




#收费接口
def free_data_interface(request):
    id = request.GET.get("id")  # 搜索重载
    order = request.GET.get("order")  # 排序方式 ： asc  desc or null
    field = request.GET.get("field")  # 排序字段
    print(id)
    if field:
        if order == "asc" or order == "":
            user_object = user_charge.objects.all().order_by("user_id")
        else:
            user_object = user_charge.objects.all().order_by("-user_id")
    else:
        if id:
            try:
                object_id = User_Info.objects.filter(user_ID=id).first()
                user_object = user_charge.objects.filter(user_id=object_id)
            except:
                pass
        else:
            user_object = user_charge.objects.all()  # 常规展示
    data_list = []
    try:
        for i in user_object:
            starttime = i.user_id.user_starttime
            endtime = i.user_id.user_endtime
            object_days = int((endtime - starttime).days)
            object_seconds = int((endtime - starttime).seconds) + object_days * 3600 * 24
            hours = int(object_seconds / 3600)
            dict = {}
            dict["userid"] = i.id
            dict["id"] = i.user_id.user_ID
            dict["free"] = str(i.user_free)
            dict["sumtime"]= str(hours)
            if i.end_free_time == None:
                end_free = ''
            else:
                end_free = i.end_free_time.strftime('%Y-%m-%d %H:%M:%S')
            dict["endtime"] = end_free
            data_list.append(dict)
    except:
        pass

    page = request.GET.get('page')  # 前端传来的页数
    limit = request.GET.get("limit")  # 前端传来的一页有几条数量

    # 分页
    paginator = Paginator(data_list, limit)
    try:
        current_page = paginator.page(page)  # 分页器进行分配
        articles = current_page.object_list  # 一个列表
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list

    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    data = {"code": 0, "msg": "", "count": user_object.count(), "data": articles}
    return JsonResponse(data, content_type="application/json")





