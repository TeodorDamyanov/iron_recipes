from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import IronRecipeUserCreateForm, LoginForm, IronRecipeUserEditForm
from .models import IronRecipeUser
# Create your views here.


class UserRegisterView(views.CreateView):
    model = IronRecipeUser
    form_class = IronRecipeUserCreateForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('index')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(views.UpdateView):
    model = IronRecipeUser
    form_class = IronRecipeUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = IronRecipeUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_like_count = sum(p.like_set.count() for p in self.object.recipe_set.all())
        recipes = self.object.recipe_set.all()
        paginator = Paginator(recipes, 2)
        page_num = self.request.GET.get('page') or 1
        page_obj = paginator.get_page(page_num)

        context.update({
            "total_like_count": total_like_count,
            "paginator": paginator,
            "page_num": page_num,
            "page_obj": page_obj,
            "recipes": recipes
        })

        return context


class UserDeleteView(views.DeleteView):  # doesnt work
    model = IronRecipeUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')

    def post(self, *args, pk):
        self.request.user.delete()
