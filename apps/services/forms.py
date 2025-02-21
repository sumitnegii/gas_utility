from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('LEAK', 'Gas Leak'),
        ('BILLING', 'Billing Inquiry'),
        ('MAINTENANCE', 'Preventive Maintenance'),
        ('OTHER', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('SUBMITTED', 'Submitted'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='service_attachments/%Y/%m/%d/', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUBMITTED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_request_type_display()} - {self.customer.email}"

class RequestUpdate(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']