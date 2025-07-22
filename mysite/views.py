from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, UpdateView, DetailView, FormView, CreateView, ListView
from mysite.forms import ContactForm
from mysite.models import Player, AddItem, Contact

# Client Admin
class ClientAdminView(TemplateView):
    template_name = 'mysite/client_admin.html'


# Page views --Template Views--
class HomeView(TemplateView):

    template_name = 'mysite/home.html'

class AboutView(TemplateView):
    template_name = 'mysite/about.html'

class SponsorView(TemplateView):
    template_name = 'mysite/sponsor.html'


class ThankYou(TemplateView):
    template_name = 'mysite/thankyou.html'


class ShopView(TemplateView):
    template_name = 'mysite/shop.html'


# --Form Views--
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'mysite/contact.html'
    # success Url
    success_url = reverse_lazy('mysite:thankyou')

    #What to do with form
    def form_valid(self, form):
        # Save the form data to the database
        Contact.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message']
        )
        print(form.cleaned_data)
        return super().form_valid(form)
    

# --CreateView--
class CreatePlayerFormView(CreateView):
    model = Player
    fields = "__all__"
    template_name = 'mysite/player_form.html'
    success_url = reverse_lazy('mysite:thankyou')

class AddItemFormView(CreateView):
    model= AddItem
    fields = '__all__'
    template_name= 'mysite/additems.html'
    success_url = reverse_lazy('mysite:thankyou')

# -- List View --

class TeamListView(ListView):
    # naming convention - template --> model_list.html
    model = Player
    context_object_name = "team_list"

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contact_messages'
    ordering = ['-created_at']  # Show newest messages first

class ShopListView(ListView):
    model = AddItem

class PlayerDetailView(DetailView):
    # Grab only one model entry
    # model_detail.html
    model = Player

    # PK --> {{teacher}}

## Update View
class PlayerUpdateView(UpdateView):
    # SHARE model_form.html
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('mysite:team')


# Delete View

class PlayerDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    # default template name: model_confirm_delete.html
    model = Player
    success_url = reverse_lazy('mysite:team')
