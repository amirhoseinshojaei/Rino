from django.shortcuts import render
from . models import (AllBrands, Services, Projects, CustomersSays, Blogs)
# Create your views here.



def index(request):
    brands = AllBrands.objects.all()
    services = Services.objects.all()
    projects = Projects.objects.all()
    customers_says = CustomersSays.objects.all()
    blogs = Blogs.objects.all()
    
    return render(request, 'core/index.html',{
        'brands': brands,
        'services': services,
        'projects': projects,
        'customers_says': customers_says,
        'blogs': blogs
    })