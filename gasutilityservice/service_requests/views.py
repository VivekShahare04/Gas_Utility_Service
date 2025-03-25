from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import ServiceRequest
from .forms import ServiceRequestForm, ServiceRequestUpdateForm

class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'service_requests/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user).order_by('-submitted_at')

class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/request_create.html'
    success_url = reverse_lazy('service_requests:dashboard')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'service_requests/request_detail.html'
    context_object_name = 'request'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRequest
    form_class = ServiceRequestUpdateForm
    template_name = 'service_requests/request_update.html'
    context_object_name = 'request'

    def get_success_url(self):
        return reverse_lazy('service_requests:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if form.instance.status == 'resolved' and not form.instance.resolved_at:
            form.instance.resolved_at = timezone.now()
        return super().form_valid(form)