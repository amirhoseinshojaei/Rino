from django.shortcuts import render
from . models import (AllBrands, Services, Projects, CustomersSays, Blogs, Counters, Skills, SkillSection,
                      ContactNumbers, CtaSection, ProjectsCategory, ServiceIntroductions, CallArea)

from django.db import models
# Create your views here.



# 



def index(request):
    brands = AllBrands.objects.all()
    services = Services.objects.all()
    projects = Projects.objects.all()
    customers = CustomersSays.objects.all()  # QuerySet of all customer records
    blogs = Blogs.objects.all()
    counters = Counters.objects.all()
    skills = Skills.objects.all()
    skill_section = SkillSection.objects.first()
    contact_numbers = ContactNumbers.objects.filter(is_staff=True)
    cta_section = CtaSection.objects.first()
    project_categories = ProjectsCategory.objects.all()
    about_section = ServiceIntroductions.objects.first()
    about_items = about_section.features.all()
    call_area = CallArea.objects.first()

    # Collect customers says with their descriptions
    customer_says_with_description = []
    for customer in customers:
        description = customer.customer_says_description.first().description if customer.customer_says_description.exists() else "پیامی در دسترس نیست"
        customer_says_with_description.append({
            'full_name': customer.full_name,
            'image': customer.image.url,
            'description': description
        })

    return render(request, 'core/index.html', {
        'brands': brands,
        'services': services,
        'projects': projects,
        'customers': customers,
        'blogs': blogs,
        'customer_says': customer_says_with_description,
        'counters': counters,
        'skills': skills,
        'skill_section': skill_section,
        'contact_numbers': contact_numbers,
        'cta_section': cta_section,
        'categories': project_categories,
        'about_section': about_section,
        'about_items': about_items,
        'call_area': call_area
    })
