from django.urls import path
from .views import HotelList, ChambreList, ReservList, ReservationView
from .views import index,index2,blog,contact,about,properties,blog_single,gallery,results,resultsprice,resultslocation,login,register,reservations,logout,rooms,reservation,payement
from .views import cancel
app_name='main'

urlpatterns = [
path('',index,name='index'),
path('home/',index,name='index'),
path('home2/',index2,name='index2'),
path('reserver/', ReservationView.as_view(), name='reservation_view'),
path('blog/',blog,name='blog'),
path('contact/',contact,name='contact'),
path('about/',about,name='about'),
path('properties/',properties,name='properties'),
path('blog_single/',blog_single,name='blog_single'),
path('gallery/',gallery,name='gallery'),
path('login/',login,name='login'),
path('register/',register,name='register'),
path('hotel_list/', HotelList.as_view(), name='HotelList'),
path('chambre_list/', ChambreList.as_view(), name='ChambreList'),
path('reservation_list/', ReservList.as_view(), name='ReservList'),
path('results/', results, name='results'),
path('rooms/', rooms, name='rooms'),
path('resultsprice/', resultsprice, name='resultsprice'),
path('resultslocation/', resultslocation, name='resultslocation'),
path('logout/',logout,name='logout'),
path('reservation/',reservation,name='reservation'),
path('payement/',payement,name='payement'),
path('reservations/',reservations,name='reservations'),
path('cancel/',cancel,name='cancel'),

]