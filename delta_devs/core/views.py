from django.shortcuts import render, redirect
from .models import User, Skill

# def project(request):
#     return render(request, 'core/project.html')
def index(request):
    return render(request,'core/index.html')
def projectlisting(request):
    return render(request,'core/projectlisting.html')
def signup(request):
    skills = Skill.objects.all()  # Fetch all available skills
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        selected_skills = request.POST.getlist('skills')  # Get the selected skills

        # Create a new user
        user = User.objects.create(username=username, email=email, password=password)

        # Add selected skills to the user
        for skill_name in selected_skills:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            user.skills.add(skill)

        # Save the user
        user.save()

        return render(request,'core/user_profile.html')  # Redirect to user profile page

    return render(request, 'core/signup.html', {'skills': skills})

def user_profile(request):
    return render(request,'core/user_profile.html')
def login(request):
    return render(request,'core/login.html')

def createproject(request):
    return render(request,'core/createproject.html')

def edit_project(request):
    return render(request,'core/edit_project.html')

def projectdetail(request):
    return render(request,'core/projectdetail.html')





