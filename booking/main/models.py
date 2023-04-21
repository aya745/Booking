from django.db import models
from django.conf import settings


# Create your models here.





class Hotel(models.Model):
	NumHot = models.AutoField(primary_key=True)
	NomHot= models.CharField(max_length=255)
	NbrEtoile= models.IntegerField()
	Desc= models.CharField(max_length=255)
	Adr= models.CharField(max_length=255)

	def __str__(self):
		return self.NomHot



class Chambre(models.Model):
	CHAMBRE_CATEGORIES = (
		('YAC', 'AC'),
		('NAC', 'NAC'),
		('DEL','DELUXE'),
		('KIN', 'KING'),
		('QUE', 'QUEEN'),
		)
	NumCh = models.AutoField(primary_key=True)
	DesChambre=models.CharField(max_length=255, default=" ")
	PrixCh = models.PositiveIntegerField(default=0)
	Superficie = models.PositiveIntegerField(default=0)
	NumEtg = models.PositiveIntegerField(default=0)
	hotel = models.ForeignKey(Hotel,to_field='NumHot', on_delete=models.CASCADE)
	categorie=models.CharField(max_length=20,choices=CHAMBRE_CATEGORIES)
	Etat=models.BooleanField(default=False)

	def __str__(self):
		return self.DesChambre
    



class Client(models.Model):

	clientt_id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=50 )
	password=models.CharField(max_length=50)
	
	email=models.CharField(max_length=50)
	phone=models.PositiveIntegerField(default=0)
	address=models.CharField(max_length=150)
	def __str__(self):
		return self.username



class Reservation(models.Model):
	IdRes=models.AutoField(primary_key=True)
	client=models.ForeignKey(Client,to_field='clientt_id', on_delete=models.CASCADE)
	hotel=models.ForeignKey(Hotel,to_field='NumHot',on_delete=models.CASCADE)
	chambre=models.ForeignKey(Chambre,to_field='NumCh',on_delete=models.CASCADE)
	DateDeb=models.DateTimeField()
	DateFin=models.DateTimeField()
	

	def __str__(self):
		return f'{self.client} has booked a {self.chambre} in Hotel {self.hotel} from {self.DateDeb} to {self.DateFin}'





class Facture(models.Model):
	IDFac = models.AutoField(primary_key=True)
	DescFac=models.CharField(max_length=300)
	PUFact=models.FloatField(default=0)
	Total=models.FloatField(default=0)
	reservation=models.ForeignKey(Reservation, to_field='IdRes',on_delete=models.CASCADE)
   

	def __str__(self):
		return self.Total


class Paiement(models.Model):
	IdPai=models.AutoField(primary_key=True)
	Mode=models.CharField(max_length=50)

	def __str__(self):
		return self.Mode


