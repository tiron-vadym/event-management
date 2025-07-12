from rest_framework.routers import DefaultRouter
from django.urls import path, include

from activity.views import EventViewSet, RegistrationViewSet

app_name = "activity"

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"registrations", RegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
