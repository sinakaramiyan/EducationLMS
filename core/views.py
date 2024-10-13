from django.urls import reverse_lazy
from django.views import generic
from core.forms import UserRegistrationForm

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')