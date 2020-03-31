# Generated by Django 2.1.4 on 2020-03-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0062_auto_20191206_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='onboarding_ticket',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='03/10/2021', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='03/10/2020', max_length=32, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('ON', 'Onboarding'), ('RU', 'Running'), ('CO', 'Completed'), ('SU', 'Suspended'), ('SD', 'Shutting down'), ('AR', 'Archived')], default='RU', max_length=2),
        ),
    ]
