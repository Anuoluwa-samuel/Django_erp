from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from inventory.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product, Category, Order, Staff 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User




class Index(TemplateView):
    template_name = 'dashboard.html'


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



@login_required
def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/base_inventory.html', {'products': products})

@login_required
def create_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            category=request.POST['category'],
            quantity=request.POST['quantity']
        )
        messages.success(request, "Product added.")
        return redirect('product_list')
    return render(request, 'inventory/create_product.html')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST['name']
        product.category = Category.objects.get(id=request.POST['category'])
        product.description = request.POST['description']
        product.quantity = request.POST['quantity']
        product.unit_price = request.POST['unit_price']
        product.save()
        return redirect('inventory_list')

    return render(request, 'inventory/edit_product.html', {'product': product, 'categories': categories})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('inventory_list')

    return render(request, 'inventory/delete_product.html', {'product': product})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'inventory/staff_list.html', {'staff': staff})

@login_required
def order_list(request):
    if request.user.is_superuser:
        orders = Order.objects.all()
    else:
        staff = Staff.objects.get(user=request.user)
        orders = Order.objects.filter(staff=staff)

    return render(request, 'inventory/order_list.html', {'orders': orders})

@login_required
def create_order(request):
    products = Product.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        Order.objects.create(
            product_id=request.POST['product'],
            quantity=request.POST['quantity'],
            staff_id=request.POST['staff'],
            status='pending'
        )
        messages.success(request, "Order created.")
        return redirect('order_list')

    return render(request, 'inventory/create_order.html', {'products': products, 'staff': staff})

@login_required
def create_staff(request):
    users = user.objects.exclude(id__in=Staff.objects.values_list('user_id', flat=True))

    if request.method == 'POST':
        Staff.objects.create(
            user_id=request.POST['user'],
            role=request.POST['role']
        )
        messages.success(request, "Staff member added.")
        return redirect('staff_list')

    return render(request, 'inventory/create_staff.html', {'users': users})

@login_required
def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        staff.role = request.POST['role']
        staff.phone = request.POST['phone']
        staff.save()
        messages.success(request, "Staff updated.")
        return redirect('staff_list')

    return render(request, 'inventory/edit_staff.html', {'staff': staff})

@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        staff.delete()
        messages.success(request, "Staff deleted.")
        return redirect('staff_list')

    return render(request, 'inventory/delete_staff.html', {'staff': staff})

@login_required
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'inventory/staff_list.html', {'staff': staff})