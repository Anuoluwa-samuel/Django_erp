from django.urls import path
from .  import views

urlpatterns = [
    path('', views.purchase_request_list, name='purchase_request_list'),
    path('request/', create_purchase_request, name='create_purchase_request'),
    path('rfq/', rfq, name='rfq'),
    path('rfq/create/', create_rfq, name='create_rfq'),
    path('quotations/', quotation_list, name='quotation_list'),
    path('quotation/submit/', submit_quotation, name='submit_quotation'),
    path('vendor/new/', create_vendor, name='create_vendor'),
    path('vendors/', vendor_list, name='vendor'),
    path('vendors/<int:pk>/edit/', edit_vendor, name='edit_vendor'),
    path('vendors/<int:pk>/delete/', delete_vendor, name='delete_vendor'),
    path('request/<int:request_id>/approve/', approve_request, name='approve_request'),
    path('request/<int:request_id>/decline/', decline_request, name='decline_request'),
    path('orders/', purchase_order_list, name='purchase_order_list'),

]
