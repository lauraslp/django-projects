from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client, Card, Pet, Visit
from .forms import RegisterForm, CardForm, ClientForm, VisitForm, PetForm


# class CardFormView(LoginRequiredMixin,CreateView):
#     model = Card
#     form_class = CardForm
#     login_url = 'vet-login'
#     template_name = 'vetapp/register_new.html'
#     # success_url = '/registration/'
#
# class ClientFormView(LoginRequiredMixin,CreateView):
#     model = Client
#     form_class = ClientForm
#     login_url = 'vet-login'
#     template_name = 'vetapp/register_new.html'

class CardDetailsView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'vetapp/card_details.html'
    login_url = 'vet-login'


class MultipleFormsView(LoginRequiredMixin, CreateView):
    template_name = 'vetapp/register_new.html'
    login_url = 'vet-login'
    model = Card
    form_classes = {
        'card': CardForm,
        'client': ClientForm,
        'pet': PetForm,
    }
    success_url = '/start-page/'

class ListCardView(LoginRequiredMixin, ListView):
    template_name = 'vetapp/registry.html'
    login_url = 'vet-login'
    model = Card
    context_object_name = 'cards'
    paginate_by = 10
    form_class = VisitForm
    # queryset = Card.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visits'] = Visit.objects.all()
        return context


def registernew(request):
    if request.method == 'POST':
        card_form = CardForm(request.POST)
        client_form = ClientForm(request.POST)
        pet_form = PetForm(request.POST)
        visit_form = VisitForm(request.POST)
        if card_form.is_valid and client_form.is_valid and pet_form.is_valid and visit_form.is_valid:
            card_form.save()
            client_form.save()
            pet_form.save()
            visit_form.save()
            messages.success(request, f'Data was saved')
        else:
            messages.error(request, f'Not all fields was filled')
    else:
        card_form = CardForm()
        client_form = ClientForm()
        pet_form = PetForm()
        visit_form = VisitForm()
    context = {
        'card_form': card_form,
        'client_form': client_form,
        'pet_form': pet_form,
        'visit_form': visit_form,
    }
    return render(request, 'vetapp/register_new.html', context=context)



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login')
        return redirect('vet-login')
    else:
         form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is inactive')
        else:
            return HttpResponse('Your username or password is incorrect! Try again.')
    return render(request, 'users/login.html', {})


def logout_user(request):
    return (request, 'users/logout.html')


@login_required
def startpage(request):
    return render(request, 'vetapp/startpage.html')

# @login_required
# def details(request):
#     return render(request, 'vetapp/card_details.html')

def reports(request):
    return render(request, 'vetapp/reports.html')

@login_required
def registry(request):
    return render(request, 'vetapp/registry.html')

@login_required
def profile(request):
    # return render(request, 'users/profile.html', {'navbar': 'profile'})
    return render(request, 'users/profile.html')


def home(request):
    return render(request, 'vetapp/home.html')


def about(request):
    return render(request, 'vetapp/about.html', {'title': about})