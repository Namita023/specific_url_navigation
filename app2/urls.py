from django.urls import path
from app2.views import *

app_name='caller'

urlpatterns=[
    path('call/',call,name='call'),
]