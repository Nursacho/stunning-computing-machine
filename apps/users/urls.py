from django.urls import path

from .views import ProfileViewSetAPI, ProfileUpdateViewSet


urlpatterns = [
    path('', ProfileViewSetAPI.as_view(), name='profiles-list'),
    path('update/<int:pk>/', ProfileUpdateViewSet.as_view())
]