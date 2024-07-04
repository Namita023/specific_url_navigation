from django.shortcuts import render

# Create your views here.

def reply(request):
    return render(request,'reply.html')