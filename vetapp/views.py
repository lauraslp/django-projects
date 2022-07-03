from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from .models import Client, Card
from .forms import RegisterForm, ClientForm, PetForm, VisitForm, CardForm

# Create your views here.

class AddPatient(LoginRequiredMixin,CreateView):
    model = Card
    form_class = CardForm
    login_url = 'vet-login'
    template_name = 'vetapp/register_new.html'
    success_url = '/registration/'

    def registernew(request):
        form = CardForm

        if form.is_valid:
            form.save()
        else:
            form = CardForm
        return render(request, 'vetapp/register_new.html', {'form': form})



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


def reports(request):
    return render(request, 'vetapp/reports.html')


def registry(request):
    return render(request, 'vetapp/registry.html')


def profile(request):
    # return render(request, 'users/profile.html', {'navbar': 'profile'})
    return render(request, 'users/profile.html')


def home(request):
    return render(request, 'vetapp/home.html')


def about(request):
    return render(request, 'vetapp/about.html', {'title': about})