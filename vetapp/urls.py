from django.urls import path
from .views import home, about, register, startpage,  AddPatient, reports, registry, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', home, name='vet-index'),
    path('about/', about, name='vet-about'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='vet-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='vet-logout'),
    path('register/', register, name='register'),
    path('start/', startpage, name='start-page'),
    path('registration/', AddPatient.as_view(), name='new-patient'),
    path('reports/', reports, name='reports'),
    path('registry/', registry, name='registry'),
    path('profile/', profile, name='user-profile'),
]