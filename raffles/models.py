from django.db import models


# Create your models here.
class Ticket(models.Model):
    STATUS_OPTIONS = [
        ("free", "Libre"),
        ("set", "Apartado"),
        ("paid", "Pagado"),
    ]

    id = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name="Número de ticket")
    status = models.CharField(
        max_length=4, choices=STATUS_OPTIONS, default="free", verbose_name="Estado"
    )
    client = models.ForeignKey(
        "Client",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Cliente",
    )
    raffle = models.ForeignKey(
        "Raffle", on_delete=models.CASCADE, related_name="tickets", verbose_name="Rifa"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"{self.number} - {self.raffle}"

    class Meta:
        verbose_name_plural = "Tickets"
        verbose_name = "Ticket"


class Raffle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    banner = models.ImageField(upload_to="banner", verbose_name="Banner")
    description = models.CharField(max_length=200, verbose_name="Descripción")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin")
    ticket_price = models.FloatField(verbose_name="Precio del ticket")
    tickets_amount = models.IntegerField(
        default=100,
        verbose_name="Cantidad de tickets",
        help_text="Cantidad de tickets a crear. Al menos 1",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rifas"
        verbose_name = "Rifa"

    def create_tickets(self):
        """ Create new free tickets for the raffle
        """
        for index in range(self.tickets_amount):
            Ticket.objects.create(
                number=index + 1,
                status="free",
                raffle=self,
            )
            
    def save(self, *args, **kwargs):
        """Override save method to run custom logic after saving the instance."""
        
        # Check if the instance is new (not yet saved to the database)
        is_new = self.pk is None
        
        # Save model instance
        super().save(*args, **kwargs)
        
        # Create tickets only if it's a new instance
        if is_new:
            self.create_tickets()


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    city = models.CharField(max_length=200, verbose_name="Ciudad")
    phone = models.CharField(
        max_length=15,
        verbose_name="Teléfono",
        help_text="Formato: 1234567890 o +34123456789",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def update_tickets_status(self, status: str, raffle: Raffle):
        """Method to reduce ticket status from an specific client

        Args:
            status (str): Status to set for the tickets (free, set, paid)
            raffle (Raffle): Raffle instance to filter tickets

        Returns:
            int: Amount of tickets updated
        """
        client_tickets = Ticket.objects.filter(client=self, raffle=raffle)
        client_tickets.update(status=status)
        client_tickets_amount = client_tickets.count()
        return client_tickets_amount