from django.urls import path
from . import views, Ajax_check, data_interface
from django.contrib.auth import views as auth_views

app_name = "My_Parking_Charge"
urlpatterns = [
    path('fo/', views.forloopd),  # 登陆url
    path('login/', views.mylogin, name="mylogin"),  # 登陆url
    path('register/', views.register, name="myregister"),  # 注册url

    path('index/', views.index, name="myindex"),  # 后台url
    # path('base/', views.base, name="base"),  # 测试url
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='user_logout'),  # 退出
    # template_name=''
    path('usual/', views.usual, name="myusual"),  # 后台常规用户url
    path('VIP/', views.VIP, name="myVIP"),  # 后台VIP用户url

    # 查看iframe页面
    path('vip_detail_iframe/', views.vip_detail_iframe, name="vip_detail_iframe"),
    # 编辑iframe页面
    path('vip_edit_iframe/', views.vip_edit_iframe, name="vip_edit_iframe"),

    # 二维码的iframe
    path('QRcode_iframe/', views.QRcode_iframe, name="QRcode_iframe"),


    path('usual_iframe/', views.usual_iframe, name="usual_iframe"),

    # VIP收费
    path('free/', views.free, name="free"),

    # Ajax 验证
    path('login_ajax/', Ajax_check.admin_login, name="admin_login"),  # ajax验证登陆url
    path('VIPdelete/', Ajax_check.VIPdelete, name="VIPdelete"),  # ajax验证登陆url
    path('VIPregister/', Ajax_check.VIPregister, name="VIPregister"),  # 会员注册ajax url
    path('VIPedit/', Ajax_check.VIPedit, name="VIPedit"),  # 会员编辑ajax url
    path('usual_add/', Ajax_check.usual_add, name="usual_add"),  # 会员编辑ajax url
    path('usualdelete/', Ajax_check.usualdelete, name="usualdelete"),  # 常规记录 ajax url

    path('usual_update/', Ajax_check.usual_update, name="usual_update"),  # 常规更新 ajax url
path('free_update/', Ajax_check.free_update, name="free_update"),  # 收费更新 ajax url



    # 数据接口

    # 常规用户数据接口
    path('usual_data_interface/', data_interface.usual_data_interface, name='usual_data_interface'),

    # 会员用户数据接口
    path('VIP__data_interface/', data_interface.VIP__data_interface, name='VIP__data_interface'),

    # 用户收费数据接口
    path('free_data_interface/', data_interface.free_data_interface, name='free_data_interface'),

]
