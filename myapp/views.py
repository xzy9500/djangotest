from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(requst):
    return HttpResponse("you did it!")

def sayhello(request):
    return HttpResponse("hello motherfucker!")

#from .models import test#
def genname(request):
    #去模板里取数据
 #   testlist = test.objects.all()
    #将数据传递给模板,第二个参数是模板路径，第三个参数是传递值的名称+值
    return render(request,'myapp/test.html',{"test":''})
    pass
