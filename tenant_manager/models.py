from django.db import models
from django_tenants.models import TenantMixin

class Tenant(TenantMixin):
    name = models.CharField
