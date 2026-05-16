from django.urls import path

from . import views

urlpatterns = [
    path('', views.uindex, name='uindex'), 
    path('ucontact', views.ucontact, name='ucontact'), 
    path('uabout', views.uabout, name='uabout'),
    path('usignup', views.usignup, name='usignup'),
    path('usignin', views.usignin, name='usignin'),
    path('ulogout', views.ulogout, name='ulogout'),
    path('uproduct', views.uproduct, name='uproduct'),
    path('resendotp', views.resendotp, name='resendotp'),
    path('uforgotpassword', views.uforgotpassword, name='uforgotpassword'),
    path('uproductdetails', views.uproductdetails, name='uproductdetails'),
    path('uprofile', views.uprofile, name='uprofile'),
    path('umyorder', views.umyorder, name='umyorder'),
    path('ucart', views.ucart, name='ucart'),
    path('uterms', views.uterms, name='uterms'),
    path('umycart', views.umycart, name='umycart'),
]