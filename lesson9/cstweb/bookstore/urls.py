from django.urls import path
from .import views

app_name='bookstore'
urlpatterns=[

#http://127.0.0.1:8000/bookstore/
path(r'',views.index,name='index'),
#http://127.0.0.1:800/bookstore/users
path('users/',views.users,name='users'),


]