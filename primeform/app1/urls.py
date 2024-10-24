from django.urls import path
from app1 import views

urlpatterns=[
    path('prime',views.func1,name='primenum')
]