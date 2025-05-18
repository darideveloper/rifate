from django.shortcuts import render
from django.views import View

from .models import Raffle, Ticket, Client


# Create your views here.
class HomeView(View):
    def get(self, request):
        raffle = Raffle.objects.all().first()
        return render(request, "raffles/index.html", {"raffle": raffle})


class TicketsView(View):
    def get(self, request):
        raffle = Raffle.objects.all().first()
        tickets = Ticket.objects.all()
        return render(
            request, "raffles/boletos.html", {"raffle": raffle, "tickets": tickets}
        )

    def post(self, request):
        name = request.POST["fullName"]
        city = request.POST["city"]
        phone = request.POST["phoneNumber"]
        email = request.POST["userEmail"]

        client = Client.objects.filter(email=email).first()
        raffle = Raffle.objects.all().firtst()
        
        if client is None:
            Client.objects.create(
                name=name, 
                city=city, 
                phone=phone, 
                email=email)
            
        else:
            Client.update_tickets_status(status="set", raffle=raffle)
