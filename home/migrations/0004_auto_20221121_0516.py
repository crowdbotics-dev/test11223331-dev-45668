# Generated by Django 2.2.28 on 2022-11-21 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aqwer_testfiled1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aqwer',
            name='testfiled1122',
        ),
        migrations.AddField(
            model_name='aqwer',
            name='testField1122',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
