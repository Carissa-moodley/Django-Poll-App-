from django.urls import path
from register import views

app_name="register"
urlpatterns = [
    path('', views.register_user, name='register_user'),
    path('logout/', views.user_logout, name='logout'),
    
]