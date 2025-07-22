from django.urls import path
from .views import HomeView, AboutView, ContactListView, TeamListView, SponsorView, PlayerDeleteView, AddItemFormView, ContactFormView, ShopListView, ThankYou, CreatePlayerFormView, ClientAdminView, PlayerDetailView, PlayerUpdateView

app_name = 'mysite'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('client_admin', ClientAdminView.as_view(), name='client_admin'),
    path('about', AboutView.as_view(), name='about'),
    path('team', TeamListView.as_view(), name='team'),
    path('create_player', CreatePlayerFormView.as_view(), name='create_player'),
    path('player_detail/<int:pk>/', PlayerDetailView.as_view(), name='detail_player'),
    path('update_player/<int:pk>', PlayerUpdateView.as_view(), name='update_player'),
    path('add_item', AddItemFormView.as_view(), name='add_item' ),
    path('sponsor', SponsorView.as_view(), name='sponsor'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('shop', ShopListView.as_view(), name='shop' ),
    path('thankyou', ThankYou.as_view(), name='thankyou'), 
    path('delete_player/<int:pk>', PlayerDeleteView.as_view(), name="delete_player"),
    path('contactform_list', ContactListView.as_view(), name='contact_list')
]
