from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import ServiceRequest

class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'services/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'services/request_detail.html'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'services/request_create.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)