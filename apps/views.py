from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("月考index")
def dev(request):
    return HttpResponse("月考dev")
def dev2(request):
    return HttpResponse("月考dev2")
