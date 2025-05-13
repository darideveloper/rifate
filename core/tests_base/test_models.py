from django.test import TestCase
from raffles import models


class RafflesDataTestCase(TestCase):
    """Base class to generate data for Raffles app"""

    def create_raffle(
        self,
        name="Test Raffle",
        start_date="2023-01-01",
        end_date="2023-12-31",
        ticket_price=10.0,
        tickets_amount=10,
    ) -> models.Raffle:
        """Create a raffle instance"""
        return models.Raffle.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            ticket_price=ticket_price,
            tickets_amount=tickets_amount,
        )

    def create_client(
        self,
        name="Test Client",
        city="Test City",
        phone="123456789",
    ) -> models.Client:
        """Create a client instance"""
        return models.Client.objects.create(
            name=name,
            city=city,
            phone=phone,
        )
