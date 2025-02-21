from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from services.models import ServiceRequest, RequestUpdate

class SupportDashboardView(UserPassesTestMixin, ListView):
    model = ServiceRequest
    template_name = 'support/dashboard.html'
    context_object_name = 'requests'
    paginate_by = 20

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return ServiceRequest.objects.all().select_related('customer')

class RequestUpdateView(UserPassesTestMixin, UpdateView):
    model = ServiceRequest
    fields = ['status']
    template_name = 'support/request_update.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        response = super().form_valid(form)
        if form.cleaned_data['status'] == 'RESOLVED':
            self.object.resolved_at = timezone.now()
            self.object.save()
        return response