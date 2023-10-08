"""delta_devs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.urls import path
# from . import views
from core.views import index, projectlisting, signup, user_profile, login, createproject, edit_project, projectdetail

urlpatterns = [
    path('', index, name='index'),
    # path('project/', project, name='project'),
    path('admin/', admin.site.urls),
    path('projectlisting/', projectlisting, name='projectlisting' ),
    path('signup/', signup, name='signup' ),
    path('user_profile/', user_profile, name='user_profile' ),
    # path('user_profile/', your_view_function_name, name='user_profile'),

    path('login/', login, name='login' ),

    path('createproject/', createproject, name='createproject' ),
    path('edit_project/', edit_project, name='edit_project' ),
    path('projectdetail/', projectdetail, name='projectdetail' ),

    
    
]
