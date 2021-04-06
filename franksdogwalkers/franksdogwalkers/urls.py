"""franksdogwalkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views


from .views import HomepageView, Signupview

urlpatterns = [
	path('', HomepageView.as_view(), name="homepage"),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('walkers/', include('walker.urls')),
    path('appointments/', include('appointment.urls')), 
    path('dogs/', include('dog.urls')),
    path('reviews/', include('review.urls')),

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"), 
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', Signupview.as_view(), name="signup"),
]
