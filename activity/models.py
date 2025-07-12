from django.db import models

from client.models import User


class Event(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="registrations"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")
