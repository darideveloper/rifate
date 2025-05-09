from django.db import models

# Create your models here.
class Ticket(models.Model):
    STATUS_OPTIONS = [
        ("FR", "Libre"),
        ("SET", "Apartado"),
        ("PD", "Pagado"),
    ]

    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS, default="FR")
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    raffle = models.ForeignKey("Raffle", on_delete=models.CASCADE, related_name="tickets")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name_plural = "Tickets"
        verbose_name = "Ticket"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"

    def update_tickets_status(self):
        """Method to reduce ticket status from an specific user

        Args:
        
        Returns:

        """
        pass

class Raffle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    banner = models.ImageField(upload_to="banner")
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    ticket_price = models.FloatField()

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
        tickets = [
        Ticket(number=i, status="FR", raffle=self)
            for i in range(1, 101)
        ]
        Ticket.objects.bulk_create(tickets)