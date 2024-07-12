from django.shortcuts import render
from item.models import Catagory, Item
from .forms import SignUpForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    catagories = Catagory.objects.all()
    context = {'catagories' : catagories , 'items' : items}
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

