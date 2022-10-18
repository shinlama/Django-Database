from django.urls import path
from .import views

# /api/users/
urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:user_pk>', views.user_detail)
]
