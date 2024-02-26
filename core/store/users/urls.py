from django.urls import path
from .views      import UserProfileView, UserCreateView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('create/',  UserCreateView.as_view(),  name='create'),
]
