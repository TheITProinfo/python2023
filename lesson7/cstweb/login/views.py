from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    data=dict()
    return render(request,'login/home.html',data)
def page_2023_view(request):
    html="<h2>this is page 2023</h2>"
    return HttpResponse(html)

def page1_view(request):
    html="<h1>this is page No.1</h1>"
    return HttpResponse(html)