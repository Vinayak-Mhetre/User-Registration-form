from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginfunction,name='login'),
    path('signup/',views.signupfunction,name='signup'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('changep/',views.change_un_pwd,name='changep')
]