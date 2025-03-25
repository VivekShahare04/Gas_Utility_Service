from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from service_requests.models import ServiceRequest

User = get_user_model()

class SupportTicket(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE, related_name='support_ticket')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.service_request.get_request_type_display()}"

    class Meta:
        ordering = ['-created_at']