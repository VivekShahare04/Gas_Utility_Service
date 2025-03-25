from django.urls import path
from .views import (
    SupportDashboardView,
    SupportTicketUpdateView,
    SupportRequestDetailView,
)

app_name = 'customer_support'

urlpatterns = [
    path('', SupportDashboardView.as_view(), name='dashboard'),
    path('ticket/<int:pk>/', SupportTicketUpdateView.as_view(), name='update_ticket'),
    path('request/<int:pk>/', SupportRequestDetailView.as_view(), name='request_detail'),
]