from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path

from raffles.views import (
    HomeView,
    TicketsView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("tickets", TicketsView.as_view(), name="tickets"),
]

if not settings.STORAGE_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)