"""egrub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customers.views import IndexPage, AboutPage, Order, ConfirmOrder, ConfirmOrderPayment, MenuList, SearchMenuList
from restaurant.views import StaffDashboard, OrderInformation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', IndexPage.as_view(), name='index'),
    path('about/', AboutPage.as_view(), name='about'),
    path('menu-list/', MenuList.as_view(), name='menu-list'),
    path('search-menu-list/', SearchMenuList.as_view(), name='search-menu-list'),
    path('order/', Order.as_view(), name='order'),
    path('order-confirm/<int:pk>', ConfirmOrder.as_view(), name='order-confirm'),
    path('confirm-order-payment/', ConfirmOrderPayment.as_view(), name='confirm-order-payment'),
    path('dashboard/', StaffDashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderInformation.as_view(), name='order-information'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
