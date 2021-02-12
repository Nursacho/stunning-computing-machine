from rest_framework.routers import DefaultRouter
from .views import (
    UserAPIViewSet,
)


router = DefaultRouter()
router.register(r'', UserAPIViewSet, basename='users')
urlpatterns = router.urls
