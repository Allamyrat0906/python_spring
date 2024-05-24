from django.urls import path
from . import views


urlpatterns=[
    path('', views.index),
    path('allmonths',views.allMonths),
    path('temp/test',views.other_temp),
    #path('<str:name>', views.dynamic_name),
    path('<str:m>',views.valueMonths,name="singleValue")
]