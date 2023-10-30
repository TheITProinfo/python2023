from django.shortcuts import render,HttpResponse

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
    return render(request,'bookstore/index_temp.html',data)


    