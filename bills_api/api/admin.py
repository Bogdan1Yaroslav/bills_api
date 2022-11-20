from django.contrib import admin
from .models import Client, Organization, Bill, Service


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "get_organizations",
    ]

    search_fields = ["name"]

    def get_organizations(self, obj):
        return "\n".join([organization.name for organization in obj.organizations.all()])


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = ["name"]


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client_name",
        "client_org",
        "bill_sum",
        "date",
        'bill_number',
        'get_services',
    ]

    ordering = ['id']

    list_filter = (
        "client_name",
        "client_org",
        'bill_number',
    )

    def get_services(self, obj):
        return "\n".join([service.name for service in obj.services.all()])


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        'created_at'
    ]
    search_fields = ["name"]
