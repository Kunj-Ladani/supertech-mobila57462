from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('category', views.category, name='category'),
    path('categoryedit', views.categoryedit, name='categoryedit'),
    path('product', views.product, name='product'),
    path('productedit', views.productedit, name='productedit'),
    path('vendor', views.vendor, name='vendor'),
    path('order', views.order, name='order'),
    path('feedback', views.feedback, name='feedback'),
    path('user', views.user, name='user'),
    path('pendingorder', views.pendingorder, name='pendingorder'),
    path('confirmorder', views.confirmorder, name='confirmorder'),
    path('completeorder', views.completeorder, name='completeorder'),
    path('cancelorder', views.cancelorder, name='cancelorder'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('orderreport', views.orderreport, name='orderreport'),
    path('productreport', views.productreport, name='productreport'),
    path('userreport', views.userreport, name='userreport'),
]