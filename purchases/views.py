from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RequestForMaterials, Vendor, RequestForQuote, QuotationReceived, PurchaseOrder
from django.contrib import messages
from .forms import VendorForm




@login_required
def create_purchase_request(request):
    if request.method == 'POST':
        item = request.POST['item']
        quantity = request.POST['quantity']
        description = request.POST.get('description', '')

        RequestForMaterials.objects.create(
            item_name=item,
            quantity=quantity,
            description=description,
            requester=request.user
        )
        messages.success(request, "Purchase request submitted.")
        return redirect('purchase_request_list')

    return render(request, 'purchases/create_request.html')


@login_required
def send_rfq(request):
    if request.method == 'POST':
        material_id = request.POST['material_request']
        vendor_id = request.POST['vendor']
        deadline = request.POST['deadline']

        material_request = get_object_or_404(RequestForMaterials, id=material_id)
        vendor = get_object_or_404(Vendor, id=vendor_id)

        RequestForQuote.objects.create(
            material_request=material_request,
            vendor=vendor,
            deadline=deadline
        )
        messages.success(request, "RFQ sent successfully.")
        return redirect('send_rfq')

    material_requests = RequestForMaterials.objects.filter(status='approved')
    vendors = Vendor.objects.all()

    return render(request, 'purchases/send_rfq.html', {
        'material_requests': material_requests,
        'vendors': vendors,
    })



@login_required
def quotation_list(request):
    quotations = QuotationReceived.objects.select_related('rfq', 'rfq__material_request', 'rfq__vendor')
    return render(request, 'purchases/quotation_list.html', {
        'quotations': quotations
    })


@login_required
def purchase_request_list(request):
    requests = RequestForMaterials.objects.all()
    return render(request, 'purchases/purchase_list.html', {'requests': requests})

@login_required
def submit_quotation(request):
    if request.method == 'POST':
        rfq = get_object_or_404(RequestForQuote, id=request.POST['rfq'])
        QuotationReceived.objects.create(
            rfq=rfq,
            quoted_price=request.POST['quoted_price'],
            delivery_time_in_days=request.POST['delivery_time'],
            notes=request.POST.get('notes', '')
        )
        messages.success(request, "Quotation submitted.")
        return redirect('quotation_list')

    rfqs = RequestForQuote.objects.all()
    return render(request, 'purchases/submit_quotation.html', {'rfqs': rfqs})

@login_required
def create_vendor(request):
    if request.method == 'POST':
        Vendor.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST.get('phone', '')
        )
        messages.success(request, "Vendor created successfully.")
        return redirect('create_vendor')

    return render(request, 'purchases/create_vendor.html')

@login_required
def approve_request(request, request_id):
    pr = get_object_or_404(RequestForMaterials, id=request_id)
    pr.status = 'approved'
    pr.save()
    messages.success(request, "Request approved.")
    return redirect('purchase_request_list')

@login_required
def decline_request(request, request_id):
    pr = get_object_or_404(RequestForMaterials, id=request_id)
    pr.status = 'declined'
    pr.save()
    messages.warning(request, "Request declined.")
    return redirect('purchase_request_list')

@login_required
def purchase_order_list(request):
    orders = PurchaseOrder.objects.all()
    return render(request, 'purchases/purchase_order_list.html', {'orders': orders})

@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'purchases/vendor.html', {'vendors': vendors})

@login_required
def vendor_edit(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'purchases/vendor_edit.html', {'form': form})

def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_delete')
    return render(request, 'purchases/vendor_delete.html', {'object': vendor})