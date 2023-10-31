from django.shortcuts import render,HttpResponse
# import created class "Userinfo"
from bookstore.models import Userinfo  

# Create your views here.
def index(request):

    html='this is bookstore home page'

    return HttpResponse('bookstore home page')

def users(request):
    data={

        'username':'cst001',
        'age':20,
        'phone':'4168337666'
    }
    # html='this is uses infomation'
    # return HttpResponse(html)
    # insert ---create
   # userinfo=Userinfo()
    # userinfo.name="Alice"
    # userinfo.age=23
    # userinfo.phone='4168889900'
    # userinfo.save()

    ## update - 
    # userinfo=Userinfo.objects.get(id=8)
    # print(userinfo.name)
    # userinfo.name="Alice_new1100"
    # userinfo.age=30
    # userinfo.phone="6168881234"
    # userinfo.save()
    
    ## delete --

    userinfo=Userinfo.objects.get(id=11)
    print("name {0}, age {1} ".format(userinfo.name,userinfo.age))
    userinfo.delete()







    return render(request,'bookstore/index_temp.html',data)


    