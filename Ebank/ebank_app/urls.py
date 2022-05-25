from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('logging_in', views.logging_in, name='logging_in'),

    path('register', views.register, name='register'),

    path('homepage', views.homepage, name='homepage'),

    path('transactions', views.transaction, name='transaction'),

    path('profile', views.profile, name='profile'),

    path('edit', views.edit_profile, name='edit'),

    path('change_password', views.change_password, name='change_password'),

    path('logging_out', views.logging_out, name='logging_out'),


]

