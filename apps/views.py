from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("月考index")
def dev(request):
    return HttpResponse("月考dev")
