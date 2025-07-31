from django.contrib import admin
from .models import Vendor, PurchaseRequest, PurchaseOrder, RequestForMaterials, RequestForQuote, QuotationReceived

admin.site.register(Vendor)
admin.site.register(PurchaseRequest)
admin.site.register(PurchaseOrder)
admin.site.register(RequestForMaterials)
admin.site.register(RequestForQuote)
admin.site.register(QuotationReceived)
