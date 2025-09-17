import json
from django.core.management.base import BaseCommand
from django_tenants.utils import schema_context, get_tenant_model
from myapp.models import Person  # change this to your model

class Command(BaseCommand):
    help = "Load JSON data into ALL tenants"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Path to JSON file")

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]
        with open(json_file) as f:
            data = json.load(f)

        Tenant = get_tenant_model()
        for tenant in Tenant.objects.all():
            with schema_context(tenant.schema_name):
                self.stdout.write(f"Loading data for tenant: {tenant.schema_name}")
                for item in data:
                    Person.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Data loaded into all tenants"))
    