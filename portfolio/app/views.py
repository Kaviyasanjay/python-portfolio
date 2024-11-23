from django.shortcuts import render
from .models import SectionContent

def home(request):
    home_content = SectionContent.objects.filter(section='home').first()
    return render(request, 'pages/home.html', {'content': home_content})

def about(request):
    about_content = SectionContent.objects.filter(section='about').first()
    return render(request, 'pages/about.html', {'content': about_content})

def education(request):
    education_content = SectionContent.objects.filter(section='education').first()
    return render(request, 'pages/education.html', {'content': education_content})

def experience(request):    
    experience_content = SectionContent.objects.filter(section='experience').first()    
    return render(request, 'pages/experience.html', {'content': experience_content})    

def contact(request):    
    contact_content = SectionContent.objects.filter(section='contact').first()    
    return render(request, 'pages/contact.html', {'content': contact_content})  