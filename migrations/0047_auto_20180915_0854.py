# Generated by Django 2.0 on 2018-09-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0046_auto_20180914_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='prj_dns',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='project-specific DNS'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='09/15/2019', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='09/15/2018', max_length=32, verbose_name='Start Date'),
        ),
    ]
