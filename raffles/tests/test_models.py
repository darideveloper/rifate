from raffles import models
from core.tests_base.test_models import RafflesDataTestCase


class RaffleTestCase(RafflesDataTestCase):
    """Test Raffle model custom methods"""

    def setUp(self):
        # Create a raffle instance
        self.raffle = self.create_raffle()

    def test_create_tickets(self):
        """Check custom method create_tickets"""

        # Delete initial tickets
        models.Ticket.objects.filter(raffle=self.raffle).delete()

        # Create tickets for the raffle
        self.raffle.create_tickets()

        # Validate tickets amount
        tickets = models.Ticket.objects.filter(raffle=self.raffle)
        self.assertEqual(tickets.count(), 10)

        # Validate tickets data
        for ticket in tickets:
            self.assertEqual(ticket.status, "free")
            self.assertEqual(ticket.raffle, self.raffle)
            self.assertTrue(ticket.number in range(1, 11))
            self.assertIsNone(ticket.user)

    def test_create_tickets_no_create_when_update(self):
        """Check custom method create_tickets when updating
        Expect no tickets created when updating an instance"""

        # delete initial tickets
        models.Ticket.objects.filter(raffle=self.raffle).delete()

        # Update raffle instance
        self.raffle.name = "Updated Raffle"
        self.raffle.save()

        # Validate tickets amount
        tickets = models.Ticket.objects.filter(raffle=self.raffle)
        self.assertEqual(tickets.count(), 0)

    def test_save(self):
        """Check custom save behavior"""

        # validate tickets created (when saving a new instance in setUp)
        tickets = models.Ticket.objects.filter(raffle=self.raffle)
        self.assertEqual(tickets.count(), 10)


class ClientTestCase(RafflesDataTestCase):
    """Test Client model custom methods"""

    def setUp(self):
        # Create a raffle instance
        self.raffle = self.create_raffle()

        # Create a client instance
        self.client = self.create_client()

    def test_update_tickets_status(self):
        """Check custom method update_tickets_status"""

        # Add tickets to the client
        self.raffle.create_tickets()
        tickets = models.Ticket.objects.filter(raffle=self.raffle)
        for ticket in tickets:
            ticket.user = self.client
            ticket.status = "set"
            ticket.save()

        # Update tickets status with method
        self.client.update_tickets_status("paid", self.raffle)

        # Validate status updated in each ticket
        for ticket in tickets:
            ticket.refresh_from_db()
            self.assertEqual(ticket.status, "paid")
            self.assertEqual(ticket.user, self.client)
