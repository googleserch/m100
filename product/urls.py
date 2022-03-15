
from xml.etree.ElementInclude import include
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage,posts,handlelogout,handlelogin,profilehandle,payment,paymenthandler,paymentsuccess,paymentfail

urlpatterns = [
                
                    path('',homepage,name='home'),
                    path('posts/<slug:url>',posts),
                    path('payment/',payment,name='payment'),
                    path('profilehandle/',profilehandle,name='profile'),
                    path('paymenthandler/',paymenthandler,name='paymenthandler'),
                    path('paymentsuccess/',paymentsuccess,name='paymentsuccess'),
                    path('paymentfail/',paymentfail,name='paymentfail'),
                    path('logout/',handlelogout,name='logout'),
                    path('login/',handlelogin,name='login'),
                   
              ] 
