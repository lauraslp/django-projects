from django.urls import path
from .views import home, about, register, startpage, reports, registry, profile, MultipleFormsView, \
    ListCardView, CardDetailsView, registernew
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', home, name='vet-index'),
    path('about/', about, name='vet-about'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'), name='vet-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='vet-logout'),
    path('register/', register, name='register'),
    path('start/', startpage, name='start-page'),
    path('registration/', registernew, name='new-card'),
    path('reports/', reports, name='reports'),
    path('registry/', ListCardView.as_view(), name='registry'),
    path('profile/', profile, name='user-profile'),
    path('details/<pk>', CardDetailsView.as_view(), name='card-details'),
]