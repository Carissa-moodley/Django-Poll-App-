from django.urls import path, include
from . import views

# URLconf
# Namespace for urlconf
app_name = 'polls'
# Map URL to views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]