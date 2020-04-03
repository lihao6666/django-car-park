from django.db import models


# from manager.models import ParkSpot
# Create your models here.

class ParkNow(models.Model):
    car_id = models.CharField(max_length=20, primary_key=True, verbose_name="车牌号")
    begin_time = models.DateTimeField(auto_now_add=True,verbose_name="进库时间")
    park = models.ForeignKey('manager.ParkSpot', verbose_name="车库", unique=True,on_delete=models.CASCADE, related_name="parks")

    def __str__(self):
        return "card_id:{}".format(self.car_id)

    class Meta:
        db_table = "park_now"
        verbose_name = "当前停车"
        verbose_name_plural = verbose_name


class ParkHis(models.Model):
    car_id = models.CharField(max_length=20, primary_key=True, verbose_name="车牌号")
    begin_time = models.DateTimeField(verbose_name="进库时间")
    park = models.ForeignKey('manager.ParkSpot', verbose_name="车库", on_delete=models.CASCADE)
    end_time = models.DateTimeField(auto_now_add=True, verbose_name="出库时间")
    money = models.FloatField(verbose_name="费用")

    class Meta:
        unique_together = ("car_id", "begin_time")
        db_table = "park_his"
        verbose_name = "停车历史"
        verbose_name_plural = verbose_name


class ErrorMess(models.Model):
    park = models.ForeignKey('manager.ParkSpot',verbose_name="车库",related_name="error",on_delete=models.CASCADE, primary_key=True)
    error_message = models.CharField(max_length=100, verbose_name="异常信息")

    class Meta:
        db_table = "error_mess"
        verbose_name = "异常信息"
        verbose_name_plural = verbose_name


class TipMess(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    tip_message = models.CharField(max_length=100, verbose_name="提示信息")

    class Meta:
        db_table = "tip_mess"
        verbose_name = "提示信息"
        verbose_name_plural = verbose_name
