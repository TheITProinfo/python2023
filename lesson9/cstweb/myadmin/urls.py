from django.urls import path
from .import views

app_name='myadmin'
urlpatterns=[

#http://127.0.0.1:8000/myadmin/
path(r'',views.index,name='index')

]