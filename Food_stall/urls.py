"""
URL configuration for Food_stall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Local_Area_Stalls import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Registration,name='Register'),
    path('Login/',views.Login_page,name='Login'),
    path('Logout/',views.Logout_page,name='Logout'),
    path('Home/',views.Home_page,name='Home'),
    path('Add_stall/',views.Add_stall,name='Add_stall'),
    path('Add_juice/',views.Add_juice,name='Add_juice'),
    path('Add_icecream/',views.Add_icecream,name='Add_icecream'),
    path('Show_stall/',views.Show_stalls,name='Show_stalls'),
    path('Juice_stalls/',views.Juice_stalls,name='Juice_stalls'),
    path('Icecream_stall/',views.Icecream_stalls,name='Icecream_stall'),
    path('edit-stall/<int:id>/', views.edit_stall, name='Edit_stall'),
    path('update_juice_stall/<int:id>/',views.update_juice_stall,name='Update_juice'),
    path('update_icecream_stall/<int:id>/',views.update_icecream_stall,name='update_icecream_stall'),
    path('delete-stall/<int:id>/', views.delete_stall, name='Delete_stall'),
    path('delete_juice_stall/<int:id>/',views.delete_juice_stall,name='delete_juice_stall'),
    path('delete_icecream_stall/<int:id>/',views.delete_icecream_stall,name='delete_icecream_stall'),
    path('Location/<int:id>/',views.Map,name='Location'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
