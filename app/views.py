from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'cdn.html')

def bootstrap1(request):
    return render(request,'localboot.html')
