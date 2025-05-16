from django.shortcuts import render
from django.views import View

from .models import Raffle, Ticket


# Create your views here.
class HomeView(View):
    def get(self, request):
        raffle = Raffle.objects.all().first()
        return render(request, "raffles/index.html", {
            "raffle": raffle}
        )


class TicketsView(View):
    def get(self, request):
        raffle = Raffle.objects.all().first()
        tickets = Ticket.objects.all()
        return render(request, "raffles/boletos.html",{
            "raffle": raffle,
            "tickets":tickets}
        )
