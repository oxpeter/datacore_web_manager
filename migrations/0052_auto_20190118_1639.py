# Generated by Django 2.1.4 on 2019-01-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0051_auto_20190117_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='01/18/2020', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='01/18/2019', max_length=32, verbose_name='Start Date'),
        ),
    ]