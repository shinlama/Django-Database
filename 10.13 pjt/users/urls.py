from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/clubs/signup', views.club_signup, name='club_signup')
]
