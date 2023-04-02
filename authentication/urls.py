from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    #path('home/', views.home, name="home"),
    #path('admin', admin.site.urls)
    path('', views.LoginPageView.as_view(), name="login"),
    path('logout', views.logout_user, name="logout"),
]
