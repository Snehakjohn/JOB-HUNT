# Generated by Django 3.1.2 on 2021-04-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Joblist', '0003_auto_20210403_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='enddate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='startdate',
            field=models.IntegerField(null=True),
        ),
    ]
