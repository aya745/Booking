from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import ListView, FormView
from .models import Hotel, Chambre, Reservation, Client, Facture
from .forms import AvailabilityForm, ProfileForm
from main.booking_functions.availability import check_availability

# Create your views here.

#def index(response, NumHot):
#	ls=Hotel.objects.get(NumHot=NumHot)
#	return render(response,"main/base.html",{"NomHot":ls.NomHot})

#def home(response):
#	return render(response,"main/home.html",{})
def index(request):
	return render(request,'index.html')

def index2(request):
	return render(request,'index2.html')

def blog(request):
	return render(request,'blog.html')

def gallery(request):
	return render(request,'gallery.html')



def properties(request):
	return render(request,'properties.html')


def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html')


def rooms(request):
	return render(request,'rooms.html')


def blog_single(request):
	return render(request,'blog_single.html')

class HotelList(ListView):
	model=Hotel

class ChambreList(ListView):
	model=Chambre

class ReservList(ListView):
	model=Reservation

class ReservationView(FormView):
	form_class= AvailabilityForm
	template_name = 'availability_form.html'


	def form_valid(self, form):
		data = form.cleaned_data
		chambre_list = Chambre.objects.filter(categorie=data['categorie_chambre'])
		available_chambres=[]
		for ch in chambre_list:
			available_chambres.append(ch)
			#if check_availability(ch, data['DateDeb'], data['DateFin']):
			#	available_chambres.append(ch)
		

		if len(available_chambres)>0:
			ch = available_chambres[0]
			reservation = Reservation.objects.create(
				client= self.request.user,
				chambre= ch,
				hotel=getattr(ch,'hotel'),
				DateDeb=data['DateDeb'],
				DateFin=data['DateFin']
			)	
			reservation.save()	
			return HttpResponse(reservation)

		else:
			return HttpResponse('All of this category of rooms are booked!! Try another one')





def results(request):

    if request.method == 'POST':

        hotel_name = request.POST['query']

        hotels = Hotel.objects.filter(NomHot__contains=hotel_name)

        context = {'username': request.session.get('username'), 'hotels': hotels}

       

    return render(request, 'properties.html', context)


def resultslocation(request):

    if request.method == 'POST':

        hotel_adress = request.POST['query']

        hotels = Hotel.objects.filter(Adr__contains=hotel_adress)

        context = {'username': request.session.get('username'), 'hotels': hotels}

       

    return render(request, 'properties.html', context)







def resultsprice(request):

    if request.method == 'POST':

        room_price = request.POST['query']

        rooms = Chambre.objects.filter(PrixCh__contains=room_price)

        context = {'username': request.session.get('username'), 'rooms': rooms}

       

    return render(request, 'rooms.html', context)


def register(request):
    RegisterForm = ProfileForm()
    context = {'RegisterForm': RegisterForm, 'username': request.session.get('username')}
    
    if request.method == 'POST':
    	
    	username=request.POST['username']
    	password=request.POST['password']
    	
    	email=request.POST['email']
    	phone=request.POST['phone']
    	address=request.POST['address']
    	profile=Client.objects.filter(username=username).count()
    	if profile == 0:
    		Client.objects.create(username=username, password=password, email=email, phone=phone, address=address)
    		return redirect('/login/')
    	else:
    		context['error']='Username deja existant'
    		return render(request, 'register.html',context)
        
    return render(request,'register.html',context)





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        client = Client.objects.filter(username=username, password=password).count()
        if client == 1:
            request.session['username'] = username
            return redirect('/home2/')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    return render(request, 'login.html', {'username' : request.session.get('username')})


def logout(request):
    del request.session['username']
    return redirect('/home/')


def reservation(request):
	ReservationForm = AvailabilityForm()
	context = {'ReservationForm': ReservationForm, 'username': request.session.get('username')}
	if request.session.get('username') is None:
		return redirect('/login/')
	if request.method == 'POST' :
		hotel=request.POST['NomHot']
		DateDeb=request.POST['DateDeb']
		DateFin=request.POST['DateFin']
		chambre=request.POST['categorie_chambre']
		
		client=Client.objects.get(username=request.session.get('username'))
		if Hotel.objects.filter(NomHot=hotel).exists():

			hotel=Hotel.objects.get(NomHot=hotel)
			if Chambre.objects.filter(categorie=chambre,hotel=hotel).exists():
				chambre=Chambre.objects.get(categorie=chambre)
				if chambre.Etat==0:

					reservation=Reservation.objects.create(hotel=hotel,DateDeb=DateDeb,DateFin=DateFin,chambre=chambre,client=client )
					DescFac='Reservation de la chambre' +chambre.DesChambre+' dans l hotel ' +hotel.NomHot
					PUFact=chambre.PrixCh
					Total=PUFact
					Facture.objects.create(DescFac=DescFac,PUFact=PUFact,Total=Total,reservation=reservation)
					chambre.Etat=1
					chambre.save()
					return redirect('/payement/')
				else:

					context['error']= 'Room unavailable'
					return render(request,'resform.html',context)
			else:

				context['error']= 'Room unavailable'
				return render(request,'resform.html',context)
		else:

			context['error']= 'Hotel unavailable'
			return render(request,'resform.html',context)
	return render(request,'resform.html',context)
		
	
def reservations(request):
	
	client=Client.objects.get(username=request.session.get('username'))
	reservations=Reservation.objects.filter(client=client)
	context = {'username': request.session.get('username'), 'reservations': reservations}
	return render(request, 'reservations.html', context)


def cancel(request):
	ReservationForm = AvailabilityForm()
	context = {'ReservationForm': ReservationForm, 'username': request.session.get('username')}
	if request.method=='POST':
		
		hotel=request.POST['NomHot']
		DateDeb=request.POST['DateDeb']
		DateFin=request.POST['DateFin']
		chambre=request.POST['categorie_chambre']
		
		client=Client.objects.get(username=request.session.get('username'))
		hotel=Hotel.objects.get(NomHot=hotel)
		chambre=Chambre.objects.get(categorie=chambre, hotel=hotel)
		if chambre.Etat==1:
			if Reservation.objects.filter(hotel=hotel,DateDeb=DateDeb,DateFin=DateFin,chambre=chambre,client=client ).exists():
				reservation = Reservation.objects.get(hotel=hotel,DateDeb=DateDeb,DateFin=DateFin,chambre=chambre,client=client )
				reservation.delete()
				chambre.Etat=0
				chambre.save()
				return redirect('/reservations/')
			
			else:

				context['error']= 'Please enter a valid reservation' 
				return render(request,'cancel.html',context)
		else :
			context['error']= 'You did not book this room' 
			return render(request,'cancel.html',context)
	return render(request,'cancel.html',context)



def payement(request):
	return render(request,'payement.html')