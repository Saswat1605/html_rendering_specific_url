from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('index2/',index2,name='index2'),
    path('index3/',index3,name='index3'),
]