from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse

# Create your views here.

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('user.login')