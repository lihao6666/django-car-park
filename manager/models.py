from django.db import models


# Create your models here.

class VipCar(models.Model):
    car_id = models.CharField(max_length=20, primary_key=True)
    vip = models.CharField(max_length=4)

    def __str__(self):
        return "car_id:{}".format(self.car_id)

    class Meta:
        db_table = "vip_car"
        verbose_name = "VIP车信息"
        verbose_name_plural = verbose_name


class ParkSpot(models.Model):
    AREA_CHOICES = (
        (0, 'A区'),
        (1, 'B区'),
        (2, 'C区'),
        (3, 'D区')
    )
    area = models.IntegerField(choices=AREA_CHOICES, default=0, verbose_name="停车区域")
    spot_num = models.IntegerField(verbose_name="车位号")

    class Meta:
        unique_together = ("area", "spot_num")
        db_table = "park_spot"
        verbose_name = "停车场"
        verbose_name_plural = verbose_name


class ParkState(models.Model):
    SPOT_STATE = (
        (0, '空闲'),
        (1, '使用'),
        (2, '异常')
    )
    park = models.OneToOneField(ParkSpot, on_delete=models.CASCADE)
    state = models.SmallIntegerField(choices=SPOT_STATE, default=0,verbose_name="停车位状态")

    class Meta:
        db_table = "park_state"
        verbose_name = "停车位状态"
        verbose_name_plural = verbose_name
