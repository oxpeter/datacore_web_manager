# Generated by Django 2.0 on 2018-03-02 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0039_auto_20180228_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='software_installed',
            field=models.ManyToManyField(blank=True, db_table='server_soft_install_tbl', related_name='software_on_server', to='dc_management.Software'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='03/01/2019', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='03/01/2018', max_length=32, verbose_name='Start Date'),
        ),
    ]
