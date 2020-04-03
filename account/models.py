from django.db import models


# Create your models here.
class Admin(models.Model):
    account = models.CharField(max_length=20, primary_key=True, verbose_name="账号")
    password = models.CharField(max_length=20, verbose_name="密码")

    def __str__(self):
        return "user:{}".format(self.account)

    class Meta:
        db_table = "admin_account"
        verbose_name = "管理员账户"
        verbose_name_plural = verbose_name
