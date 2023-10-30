from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # html='this is myadmin homeage'
    # return HttpResponse(html)
    data=dict()

    return render(request,'myadmin/index_temp.html',data)