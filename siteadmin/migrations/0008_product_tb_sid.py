# Generated by Django 2.2.7 on 2020-01-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0007_admin_tb_cart_tb_product_tb_userregister_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='sid',
            field=models.ForeignKey(default='1', on_delete='CASCADE', to='siteadmin.SupplierRegister_tb'),
        ),
    ]
