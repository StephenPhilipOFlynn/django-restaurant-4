from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AccountUserCreationForm, AccountAuthenticationForm
from reserve.models import TableReservation

# Create your views here.

