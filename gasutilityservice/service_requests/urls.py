from django.urls import path
from .views import (
    ServiceRequestListView,
    ServiceRequestCreateView,
    ServiceRequestDetailView,
    ServiceRequestUpdateView,
)

app_name = 'service_requests'

urlpatterns = [
    path('', ServiceRequestListView.as_view(), name='dashboard'),
    path('new/', ServiceRequestCreateView.as_view(), name='create'),
    path('<int:pk>/', ServiceRequestDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', ServiceRequestUpdateView.as_view(), name='update'),
]