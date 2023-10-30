from django.urls import path

from PracticeApp6 import views


urlpatterns = [
    path('', views.home_fun),
    path('read', views.read_fun),
    path('disp', views.disp_fun),
]