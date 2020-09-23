"""cattalist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
admin.autodiscover() 
from django.urls import path, include
from pages import views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/',include('listing.urls')),
    path('dashboard', include('dashboard.urls')),
    path('app/', views.home, name="home"),
    path('',views.landing, name="landing"),
    path('about/',views.about, name="about"),
    path('Signup/', register, name='register'),
    path('Login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('Logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
