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
    user = models.ForeignKey(
        "Client",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Cliente",
    )
    raffle = models.ForeignKey(
        "Raffle", on_delete=models.CASCADE, related_name="tickets", verbose_name="Rifa"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return f"{self.number} - {self.raffle}"

    class Meta:
        verbose_name_plural = "Tickets"
        verbose_name = "Ticket"


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre completo")
    city = models.CharField(max_length=200, verbose_name="Ciudad")
    phone = models.CharField(
        max_length=15,
        verbose_name="Teléfono",
        help_text="Formato: 1234567890 o +34123456789",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def update_tickets_status(self):
        """Method to reduce ticket status from an specific user

        Args:

        Returns:

        """
        pass


class Raffle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    banner = models.ImageField(upload_to="banner", verbose_name="Banner")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin")
    ticket_price = models.FloatField(verbose_name="Precio del ticket")
    tickets_amount = models.IntegerField(
        default=100,
        verbose_name="Cantidad de tickets",
        help_text="Cantidad de tickets a crear. Al menos 1",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Detectar si es una instancia nueva
        super().save(*args, **kwargs)
        if is_new:
            self.create_tickets()

    class Meta:
        verbose_name_plural = "Rifas"
        verbose_name = "Rifa"

    def create_tickets(self):
        """Method to create the whole amount of tickets when you create a Raffle

        Args:

        Returns:

        """
        tickets = [Ticket(number=i, status="FR", raffle=self) for i in range(1, 101)]
        Ticket.objects.bulk_create(tickets)
