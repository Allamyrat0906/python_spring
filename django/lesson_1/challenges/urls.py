from django.urls import path
from . import views

urlpatterns=[
    # path('', views.index),
    # path('test1',views.test1)
    path('',views.index), # main page keep store some data
    #path('<int:month>',views.month_number), #single page uses number route
    path('<int:month_re>',views.month_number_reverse,name='reverse_month'), #single page uses number route
    path('<str:month>', views.month_string, name="months_challenges") # single page uses string
]