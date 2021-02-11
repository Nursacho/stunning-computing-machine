from django.urls import path

from .views import ProfileViewSetAPI, ProfileUpdateViewSet, ProfileDetail


urlpatterns = [
    path('', ProfileViewSetAPI.as_view(), name='profiles-list'),
    path('update/<int:pk>/', ProfileUpdateViewSet.as_view()),
    path('<int:pk>/', ProfileDetail.as_view())
]