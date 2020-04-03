# Generated by Django 2.2.1 on 2019-11-14 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20191114_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkhis',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ParkSpot', verbose_name='车库'),
        ),
        migrations.AlterField(
            model_name='parknow',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parks', to='manager.ParkSpot', verbose_name='车库'),
        ),
    ]