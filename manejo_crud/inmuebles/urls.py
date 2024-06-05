
from django.urls import path
from .views import index, register
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',index, name='Index'),
    #se traen vistas login y logout del modelo
    path('login/', LoginView.as_view(next_page='Index'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout'),
    path('register/', register, name='register')
    
]   
