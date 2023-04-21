import datetime
from main.models import Hotel,Chambre, Reservation

def check_availability(chambre,DateDeb,DateFin):
	avail_list=[]
	res_list=Reservation.objects.filter(chambre=chambre)
	for res in res_list:
		if res.DateDeb > DateFin or res.DateFin < DateDeb:
			avail_list.append(True)
		else:
			avail_list.append(False)

	return all(avail_list)      #returns true if all is true
