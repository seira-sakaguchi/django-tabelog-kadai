from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import StoreInfo
from accounts.models import CustomUser
from .forms import ProfileForm
from django.urls import reverse_lazy

class TopView(generic.ListView):
    model = StoreInfo
    template_name = 'top.html'

class StoreDetailView(generic.DetailView):
    model = StoreInfo
    template_name = 'store_detail.html'

class ProFileView(TemplateView):
    model = CustomUser
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('gourmet:profile')

