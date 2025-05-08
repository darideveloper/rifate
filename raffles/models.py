from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.IntegerField()

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

class Ticket(models.Model):
    STATUS_OPTIONS = [
        ("FR", "Free"),
        ("SET", "Set"),
        ("PD", "Paid"),
    ]

    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS, default="JR")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = "Tickets"
        verbose_name = "Ticket"

class Raffle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    banner = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    ticket_price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rifas"
        verbose_name = "Rifa"

    def create_tickets(self):
        """Method to create the whole amount of tickets when you create a Raffle

        Args:
        
        Returns:

        """
        pass