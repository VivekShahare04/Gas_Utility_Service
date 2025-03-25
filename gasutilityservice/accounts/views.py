from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('service_requests:dashboard')

    def form_valid(self, form):
        user = form.save()
        user.is_customer = True  # Default to customer role
        user.save()
        login(self.request, user)
        return redirect(self.success_url)

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_support_rep:
                return redirect('customer_support:dashboard')
            return redirect('service_requests:dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def account_landing(request):
    return render(request, 'accounts/landing.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')