from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from inventory.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


class Index(TemplateView):
    template_name = 'dashboard.html'


class Dashboard(View):
    def get(self, request):
        return render(request, 'inventory/dashboard.html')

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})

    def post(self, request): 
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect ('index')
        return render(request, 'inventory/signup.html', {'form': form}) 
