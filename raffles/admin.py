from django.contrib import admin
from raffles import models


# Register your models here.
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "phone", "created_at", "updated_at")
    search_fields = ("name", "city", "created_at", "updated_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("number", "status", "user", "created_at", "updated_at")
    search_fields = ("number", "status", "created_at", "updated_at")
    list_filter = ("status",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(models.Raffle)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at", "ticket_price")
    search_fields = ("name", "created_at", "updated_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )
