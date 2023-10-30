from django.urls import path
from .import views

app_name='login'
urlpatterns=[
    #https://127.0.0.1/login/ 
    path(r'',views.home,name='home'),
    # http://127.0.0.1/login/page/2023/
    path(r'page/2023',views.page_2023_view),

    #http://127.0.0.1/login/page/1
    path(r'page/1/',views.page1_view)




]