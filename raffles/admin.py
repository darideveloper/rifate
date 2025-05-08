from django.contrib import admin
from raffles import models

# Register your models here.
@admin.register(models.User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone')
    search_fields = ('name','city')

@admin.register(models.Ticket)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'user', 'created_at', 'updated_at')
    search_fields = ('number','status')
    list_filter = ('status',)

@admin.register(models.Raffle)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'ticket_price')
    search_fields = ('name',)
