from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import AccountUserCreationForm, AccountAuthenticationForm
from reserve.models import TableReservation

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = AccountUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = AccountUserCreationForm()
    return render(request, 'Accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AccountAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=User.objects.get(email=email).username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')
    else:
        form = AccountAuthenticationForm()
    return render(request, 'Accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

def profile_view(request):
    bookings = TableReservation.objects.filter(email=request.user.email)
    return render(request, 'Accounts/profile.html', {'bookings': bookings})

def delete_booking(request, booking_id):
    booking = get_object_or_404(TableReservation, id=booking_id, email=request.user.email)
    if request.method == 'POST':
        booking.delete()
        return redirect('accounts:profile')
    return render(request, 'accounts/confirm_delete.html', {'booking': booking})
