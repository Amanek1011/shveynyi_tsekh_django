from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'zakroyschik':
            return reverse_lazy('zakroi_home')
        else:
            return reverse_lazy('shveya_home')

def users_home(request):
    return render(request, 'users/users_home.html')