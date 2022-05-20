from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'marks'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('home/',views.home,name='home'),
    path('mapping', views.mapping, name='mapping'),
    path('iamarks', views.iamarks, name='iamarks'),
    path('mentor', views.mentor, name='mentor'),
    path('report/<int:id>', views.report, name='report'),
    path('',views.home,name='home'),
]
