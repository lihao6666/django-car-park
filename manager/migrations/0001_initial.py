# Generated by Django 2.2.1 on 2019-11-14 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField(choices=[(0, 'A区'), (1, 'B区'), (2, 'C区'), (3, 'D区')], default=0, verbose_name='停车区域')),
                ('spot_num', models.IntegerField(verbose_name='车位号')),
            ],
            options={
                'verbose_name': '停车场',
                'verbose_name_plural': '停车场',
                'db_table': 'park_spot',
                'unique_together': {('area', 'spot_num')},
            },
        ),
        migrations.CreateModel(
            name='VipCar',
            fields=[
                ('car_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('vip', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'VIP车信息',
                'verbose_name_plural': 'VIP车信息',
                'db_table': 'vip_car',
            },
        ),
        migrations.CreateModel(
            name='ParkState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.SmallIntegerField(choices=[(0, '空闲'), (1, '使用'), (2, '异常')], default=0, verbose_name='停车位状态')),
                ('park', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.ParkSpot')),
            ],
            options={
                'verbose_name': '停车位状态',
                'verbose_name_plural': '停车位状态',
                'db_table': 'park_state',
            },
        ),
    ]
