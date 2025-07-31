from django.shortcuts import render, redirect
from inventory.models import Staff
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages



# Create your views here.

def dashboard_view(request):
    modules = [
        {"name": "Inventory", "url": "/inventory/", "desc": "Manage product items"},
        {"name": "Purchases", "url": "/purchases/", "desc": "Manage purchase orders"},
        {"name": "HR", "url": "/hr/", "desc": "Human Resources"},
        {"name": "Stock", "url": "/stock/", "desc": "Stock level tracking"},
        {"name": "Accounting", "url": "/accounting/", "desc": "Financial operations"},
    ]
    return render(request, "dashboard.html", {"modules": modules})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    modules = [
        {"name": "Inventory", "url": "/inventory/", "desc": "Manage product items"},
        {"name": "Purchases", "url": "/purchases/", "desc": "Manage purchase orders"},
        {"name": "HR", "url": "/hr/", "desc": "Human Resources"},
        {"name": "Stock", "url": "/stock/", "desc": "Stock level tracking"},
        {"name": "Accounting", "url": "/accounting/", "desc": "Financial operations"},
    ]
    return render(request, "dashboard.html", {"modules": modules})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            Staff.objects.create(
                user=user,
                role='Store Assistant',  # Default role (you can make it dynamic later)
                phone='0000000000'       # You can add phone to the form if needed
            )
            messages.success(request, 'Account created successfully! You can now log in.')

            # Redirect to login page
            return redirect('login')
            # login(request, user)
            # return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

class signup_View(request):
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