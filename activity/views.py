from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from activity.models import Event, Registration
from activity.serializers import EventSerializer, RegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["date", "location", "organizer"]
    search_fields = ["title", "description"]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        registration = serializer.save(user=self.request.user)
        send_mail(
            subject="Event Registration Confirmation",
            message=(
                f"Thank you for registering for {registration.event.title}"
            ),
            from_email="managementevent36@gmail.com",
            recipient_list=[registration.user.email],
        )
