# Generated by Django 2.2.7 on 2020-01-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0005_supplierregister_tb_contactnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierregister_tb',
            name='password',
            field=models.CharField(default='4', max_length=30),
        ),
        migrations.AddField(
            model_name='supplierregister_tb',
            name='username',
            field=models.CharField(default='3', max_length=30),
        ),
        migrations.AlterField(
            model_name='supplierregister_tb',
            name='status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
