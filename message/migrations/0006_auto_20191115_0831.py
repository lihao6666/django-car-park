# Generated by Django 2.2.1 on 2019-11-15 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20191115_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errormess',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='error', serialize=False, to='manager.ParkSpot', verbose_name='车库'),
        ),
    ]
