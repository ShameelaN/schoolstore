from django.urls import path, include
from . import views
app_name='stores'
urlpatterns = [
    path('',views.shop,name='shop'),
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
    path('product',views.product,name='product'),
    ]