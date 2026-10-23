from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
def contacts(request):
    return render(request,'myapp/contacts.html')
def educations(request):
    return render(request,'myapp/educations.html')
def skills(request):
    return render(request,'myapp/skills.html')
def projects(request):
    return render(request,'myapp/projects.html')