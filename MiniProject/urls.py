"""MiniProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from siteadmin import views as admin_view
from user import views as user_view
from supplier import views as supplier_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',admin_view.Index),
    url(r'^SupplierRegister/',admin_view.SupplierRegister, name='SupplierRegister'),
    url(r'^SupplierRegisterAction/',admin_view.SupplierRegisterAction, name='SupplierRegisterAction'),
    url(r'^Login/',admin_view.Login, name='Login'),
    url(r'^LoginAction/',admin_view.LoginAction, name='LoginAction'),
    url(r'^ViewSuppliers/',admin_view.ViewSuppliers, name='ViewSuppliers'),
    url(r'^getstate/',admin_view.getstate,name='getstate'),
    url(r'^getdistrict/',admin_view.getdistrict,name='getdistrict'),
    url(r'^Reject/(?P<uid>\d+)/$',admin_view.Reject,name='Reject'),
    url(r'^Approve/(?P<uid>\d+)/$',admin_view.Approve,name='Approve'),
    url(r'^AddProduct/',admin_view.AddProduct,name='AddProduct'),
    url(r'^AddProductAction/',admin_view.AddProductAction,name='AddProductAction'),
    url(r'^UserRegisterAction/',admin_view.UserRegisterAction,name='UserRegisterAction'),
    url(r'^ViewProducts/',admin_view.ViewProducts,name='ViewProducts'),
    url(r'^UsrRegister/',admin_view.UserRegister,name='UserRegister'),
    url(r'^AddtoCart/(?P<uid>\d+)/$',admin_view.AddtoCart,name='AddtoCart'),
    url(r'^CartAction/',admin_view.CartAction,name='CartAction'),
    url(r'^ViewCart/',admin_view.ViewCart,name='ViewCart'),
    url(r'^OrderAction/',admin_view.OrderAction,name='OrderAction'),
    url(r'^ViewOrder/',admin_view.ViewOrder,name='ViewOrder'),
    url(r'^approverejectorder/',admin_view.approverejectorder,name='approverejectorder'),
    url(r'^ViewMyProducts/',admin_view.ViewMyProducts,name='ViewMyProducts'),
    url(r'^Search/',admin_view.Search,name='Search'),
    url(r'^getdata/',admin_view.getdata,name='getdata'),
    url(r'^Searchbysupplier/',admin_view.Searchbysupplier,name='Searchbysupplier'),
    url(r'^getdatas/',admin_view.getdatas,name='getdatas'),
    url(r'^Searchbyrate/',admin_view.Searchbyrate,name='Searchbyrate'),
    url(r'^getrate/',admin_view.getrate,name='getrate'),
    url(r'^ViewmyOrders/',admin_view.ViewmyOrders,name='ViewmyOrders'),
    url(r'^deletep/(?P<uid>\d+)/$',admin_view.deletep,name='deletep'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

