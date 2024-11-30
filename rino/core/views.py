from django.shortcuts import render, get_object_or_404
from . models import (AllBrands, Services, Projects, CustomersSays, Blogs, Counters, Skills, SkillSection,
                      ContactNumbers, CtaSection, ProjectsCategory, ServiceIntroductions, CallArea, TeamMembers, FAQ)

from django.db import models
from django.contrib import messages
from django.http import Http404
# Create your views here.






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



def about(request):
    team_members = TeamMembers.objects.filter(status=True)
    faqs = FAQ.objects.all()

    return render(request, 'core/about.html',{
        'team': team_members,
        'faq': faqs
    })



def comming_soon(request):
    return render (request, 'core/comming_soon.html',{})




def services(request):
    services = Services.objects.all()
    return render(request, 'core/services.html',{
        'services':services
    })




def service_detail(request, slug):
    try:
        service = get_object_or_404(Services, slug=slug)
        services = Services.objects.all().order_by('-date_added')[:4]
        images = service.images.all()
        return render(request, 'core/service_detail.html', {
            'service':service,
            'services':services,
            'images':images
        })
    
    except Http404:
        messages.error(request,'صفحه مورد نظر یافت نشد')
        return render(request,'404.html', status=404)




def team_members(request):
    team = TeamMembers.objects.filter(status=True)
    return render(request, 'core/team.html', {
        'team': team
    })




def team_member_detail(request, full_name):
    try:
        member = get_object_or_404(TeamMembers, full_name=full_name)
        return render(request, 'core/team_member_detail.html', {
            'member':member
        })
    
    except Http404:
        messages.error(request, 'صفحه مورد نظر یافت نشد')
        return render(request, '404.html', status=404)
