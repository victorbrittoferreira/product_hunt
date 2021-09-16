from django.shortcuts import render, get_object_or_404

#from .models import Account

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO route to HP and run logout

    #return render(request, 'accounts/home.html')
    return render(request, 'accounts/signup.html')