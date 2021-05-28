from django.contrib import admin, messages

from .models import *
# Register your models here.

@admin.register(VIPuserInfo)
class UserInfo1(admin.ModelAdmin):
    list_display=('user_nanme', 'user_sex', 'user_grade')
    search_fields = ('user_nanme',)
    # 增加自定义按钮(两个按钮)
    actions = ['make_copy', 'custom_button','url_button']

    def custom_button(self, request, queryset):
        pass
  # 显示的文本，与django admin一致
    custom_button.short_descriptio ='测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'
# 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):

        messages.add_message(request, messages.SUCCESS, '操作成功123123123123')

    # 给按钮增加确认
    make_copy.confirm = '你是否执意要点击这个按钮？'

    make_copy.short_description = '复制员工'

    def url_button(self,request,queryset):
       pass

    url_button.short_description='链接按钮'
    url_button.type='primary'
    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。

    url_button.action_type = 2
    url_button.action_url = 'http://www.baidu.com'




@admin.register(User_Info)
class UserInfo2(admin.ModelAdmin):
    pass


@admin.register(user_charge)
class UserInfo3(admin.ModelAdmin):
   pass
