from django.urls import path
from app1.views import *

app_name='receiver'

urlpatterns=[
    path('reply/',reply,name='reply'),
]