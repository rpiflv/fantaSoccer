from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('fanta_soccer_app:new_squad')
    template_name = 'registration/signup.html'


