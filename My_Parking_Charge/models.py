from django.db import models


# Create your models here.


class VIPuserInfo(models.Model):  # 会员用户信息注册表
    user_nanme = models.CharField(max_length=30, verbose_name="用户昵称", null=False, blank=False)
    user_ID = models.CharField(max_length=50, verbose_name="用户车牌号", unique=True, null=False, blank=False)
    uer_rank = models.IntegerField(default=1, null=False, blank=False, verbose_name="会员等级")
    user_phone = models.CharField(max_length=20, verbose_name="用户手机号", null=False, blank=False)
    user_birth = models.DateField(verbose_name="用户出生年月日", null=False, blank=False)
    user_sex = models.CharField(max_length=6, verbose_name="用户性别", null=False, blank=False)
    user_grade = models.CharField(max_length=10, verbose_name="用户年龄", null=False, blank=False)

    class meta:
        verbose_name = "会员用户注册"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_ID


class User_Info(models.Model):  # 往来用户记录信息表
    GENDER_CHOICE = (("0","常规用户"), ("1", "会员"))
    user_ID = models.CharField(max_length=50, verbose_name="用户车牌号", null=False, blank=False)
    user_choise = models.CharField(choices=GENDER_CHOICE,verbose_name="是否会员",max_length=10)
    user_starttime = models.DateTimeField(verbose_name="停车时间", blank=True, null=True, auto_now_add=False)
    user_endtime = models.DateTimeField(verbose_name="结束停车时间", blank=True, null=True,auto_now_add=False )



    class meta:
        verbose_name = "往来用户记录信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_ID







class user_charge(models.Model):  #往来用户收费表
    user_id = models.ForeignKey("User_Info",on_delete=models.CASCADE,verbose_name="用户外键",related_name="us")
    user_free = models.CharField(max_length=60,verbose_name="产生费用",blank=True,null=True)
    end_free_time = models.DateTimeField(verbose_name="清算费用时间",blank=True,null=True)


    class meta:
        verbose_name = "往来用户收费表"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.user_id
