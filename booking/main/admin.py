from django.contrib import admin
from .models import Hotel, Chambre, Facture, Reservation, Client, Paiement
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Chambre)
admin.site.register(Reservation)
admin.site.register(Facture)
admin.site.register(Client)
admin.site.register(Paiement)
