from django import forms

class AvailabilityForm(forms.Form):
	CHAMBRE_CATEGORIES = (
		('YAC', 'AC'),
		('NAC', 'NAC'),
		('DEL','DELUXE'),
		('KIN', 'KING'),
		('QUE', 'QUEEN'),
		)
	categorie_chambre=forms.ChoiceField(choices=CHAMBRE_CATEGORIES, required=True)
	DateDeb = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ]) 
	DateFin = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
	NomHot = forms.CharField(max_length=255)

class ProfileForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)