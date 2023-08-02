from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy

from .forms import IronRecipeUserCreateForm
from .models import IronRecipeUser
# Create your views here.


class UserRegisterView(views.CreateView):
    model = IronRecipeUser
    form_class = IronRecipeUserCreateForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('login')
