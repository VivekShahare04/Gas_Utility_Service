from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from service_requests.models import ServiceRequest
from .models import SupportTicket
from .forms import SupportTicketForm

class SupportDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ServiceRequest
    template_name = 'customer_support/dashboard.html'
    context_object_name = 'requests'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_support_rep

    def get_queryset(self):
        queryset = ServiceRequest.objects.all().order_by('-submitted_at')
        
        # Filter by status if provided
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
            
        # Filter by request type if provided
        request_type = self.request.GET.get('request_type')
        if request_type:
            queryset = queryset.filter(request_type=request_type)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', '')
        context['request_type_filter'] = self.request.GET.get('request_type', '')
        return context

class SupportTicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SupportTicket
    form_class = SupportTicketForm
    template_name = 'customer_support/ticket_update.html'
    context_object_name = 'ticket'

    def test_func(self):
        return self.request.user.is_support_rep

    def get_success_url(self):
        return reverse_lazy('customer_support:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_request'] = self.object.service_request
        return context

class SupportRequestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ServiceRequest
    template_name = 'customer_support/request_detail.html'
    context_object_name = 'request'

    def test_func(self):
        return self.request.user.is_support_rep

# Create your views here.
