from django.shortcuts import render
from products.models import Product
from accounts.views import login_page,register_page , activate_email



def index(request):

    context = {'products' : Product.objects.all()}
    return render(request , 'home/index.html' , context)