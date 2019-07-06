
from django.urls import path,re_path
from . import views

urlpatterns = [
        path(r'hello/',views.sayhello),
        path(r'allname/',views.genname),
        re_path(r'^$',views.index),
    ]
