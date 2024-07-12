from django.shortcuts import render, redirect
from item.models import Catagory, Item
from .forms import SignUpForm
from django.contrib.auth import logout
from django.http import HttpResponse
# Create your views here.
def index(request):    
    items = Item.objects.filter(is_sold = False)[0:6]
    catagories = Catagory.objects.all()
    context = {'catagories' : catagories , 'items' : items}
    return render(request, 'core/index.html', context)

def orders(request):
    return render(request, 'core/orders.html')

def signup(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else: 
            form = SignUpForm()
            context = {'form' : form}
            return render(request, 'core/signup.html' , context)
        
def logout_view(request):
    logout(request)
    return redirect('/login/')
