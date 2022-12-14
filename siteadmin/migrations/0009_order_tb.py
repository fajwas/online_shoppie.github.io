# Generated by Django 2.2.7 on 2020-01-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0008_product_tb_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.Cart_tb')),
                ('productid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.Product_tb')),
                ('supplierid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.SupplierRegister_tb')),
                ('userid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.UserRegister_tb')),
            ],
        ),
    ]
