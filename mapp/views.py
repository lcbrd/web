from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.method == 'GET':
        #print("GETyes")
        return render(request,'index.html')
    else:
        uid = request.POST.get('Uid','')
        pwd =request.POST.get('Pwd','')
        user = authenticate(request, username=uid, password=pwd)
        if user is not None:
            return render(request,'index.html')
        else:
            return None
def home(request):
    return render(request,'home.html')
def main(request):
    return render(request,'main.html')