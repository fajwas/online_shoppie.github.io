# Generated by Django 2.2.7 on 2020-01-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_auto_20200114_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('specification', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='')),
                ('rate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contactnumber', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete='CASCADE', to='siteadmin.Country_tb')),
                ('district', models.ForeignKey(on_delete='CASCADE', to='siteadmin.District_tb')),
                ('state', models.ForeignKey(on_delete='CASCADE', to='siteadmin.State_tb')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=30)),
                ('totalcost', models.CharField(max_length=30)),
                ('productid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.Product_tb')),
                ('sid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.SupplierRegister_tb')),
                ('userid', models.ForeignKey(on_delete='CASCADE', to='siteadmin.UserRegister_tb')),
            ],
        ),
    ]
