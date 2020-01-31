# Generated by Django 2.1.4 on 2019-12-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0061_auto_20191022_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='12/05/2020', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='12/06/2019', max_length=32, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='storage',
            field=models.ManyToManyField(blank=True, to='dc_management.Storage'),
        ),
    ]