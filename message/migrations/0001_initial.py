# Generated by Django 2.2.1 on 2019-11-14 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorMess',
            fields=[
                ('park', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='manager.ParkSpot', verbose_name='车库')),
                ('error_message', models.CharField(max_length=100, verbose_name='异常信息')),
            ],
            options={
                'verbose_name': '异常信息',
                'verbose_name_plural': '异常信息',
                'db_table': 'error_mess',
            },
        ),
        migrations.CreateModel(
            name='TipMess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('tip_message', models.CharField(max_length=100, verbose_name='提示信息')),
            ],
            options={
                'verbose_name': '提示信息',
                'verbose_name_plural': '提示信息',
                'db_table': 'tip_mess',
            },
        ),
        migrations.CreateModel(
            name='ParkNow',
            fields=[
                ('car_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='车牌号')),
                ('begin_time', models.DateTimeField(verbose_name='进库时间')),
                ('park', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.ParkSpot', verbose_name='车库')),
            ],
            options={
                'verbose_name': '当前停车',
                'verbose_name_plural': '当前停车',
                'db_table': 'park_now',
            },
        ),
        migrations.CreateModel(
            name='ParkHis',
            fields=[
                ('car_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='车牌号')),
                ('begin_time', models.DateTimeField(verbose_name='进库时间')),
                ('end_time', models.DateTimeField(verbose_name='出库时间')),
                ('money', models.FloatField(verbose_name='费用')),
                ('park', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.ParkSpot', verbose_name='车库')),
            ],
            options={
                'verbose_name': '停车历史',
                'verbose_name_plural': '停车历史',
                'db_table': 'park_his',
                'unique_together': {('car_id', 'begin_time')},
            },
        ),
    ]
