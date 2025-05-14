from django.contrib import admin
from raffles import models


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("number", "status", "client", "raffle", "created_at", "updated_at")
    search_fields = ("number", "client__name", "client__city", "client__phone")
    list_filter = ("status", "raffle", "updated_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "phone", "updated_at")
    search_fields = ("name", "city", "phone")
    list_filter = ("created_at", "updated_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(models.Raffle)
class RaffleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "start_date",
        "ticket_price",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
