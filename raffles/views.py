from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Raffle, Ticket, Client
import json


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
        data = json.loads(request.body)
        
        name = data.get("fullName")
        city = data.get("city")
        phone = data.get("phoneNumber")
        email = data.get("userEmail")
        tickets = data.get("selectedTickets")
        tickets = tickets.split(", ")
        print(tickets)

        client = Client.objects.all().filter(email=email).first()
        raffle = Raffle.objects.all().first()

        if client is None:
            client = Client.objects.create(name=name, city=city, phone=phone, email=email)

        else:
            pass
        
        for ticket_number in tickets:
            ticket =  Ticket.objects.get(number=ticket_number)
            ticket.status = "set"
            ticket.client = client
            ticket.raffle = raffle
            ticket.save()

        
        return JsonResponse({"message": "Datos recibidos correctamente"}, status=200)

 