# Generated by Django 2.1.4 on 2019-07-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0056_auto_20190618_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='account_number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='07/08/2020', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='07/09/2019', max_length=32, verbose_name='Start Date'),
        ),
    ]
