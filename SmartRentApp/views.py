from datetime import timezone
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from SmartRentApp.models import Booking, Accommodation, Member


# Create your views here.


def register(request):
    if request.method == "POST":
        member = Member(firstname=request.POST['firstname'],
                        surname=request.POST['surname'],
                        email=request.POST['email'],
                        username=request.POST['username'],
                        password=request.POST['password']
                        )
        return render(request, 'login.html')
    else:

        return render(request, 'register.html')


def login(request):
    # if Member.objects.filter(username=request.POST['username'], email=request.POST['email'],
    #                          password=request.POST['password']).exists():
    #     Member.objects.filter(username=request.POST['username'],
    #                           email=request.POST['email'],
    #                           password=request.POST['password'])
    #     return render(request, 'index.html')
    # else:
    return render(request, 'login.html')


# if request.method == "POST":
#     # Use the get() method to avoid MultiValueDictKeyError
#     username = request.POST.get('username', '')
#     email = request.POST.get('email', '')
#     password = request.POST.get('password', '')
#
#     # Check if a Member with the provided username, email, and password exists
#     if Member.objects.filter(username=username, email=email, password=password).exists():
#         # Authentication successful
#         return render(request, 'index.html')
#     else:
#         # Authentication failed
#         return render(request, 'login.html')

# return render(request, 'login.html')


def reset(request):
    return render(request, 'reset.html')


def index(request):
    return render(request, 'index.html')


def accommodations(request):
    return render(request, 'accommodation.html')


# @login_required
def book_accommodation(request, accommodation_id):
    accommodation = Accommodation.objects.get(pk=accommodation_id)
    commission_percentage = 0.45
    commission = accommodation.price * commission_percentage

    # Save booking information
    expiration_time = timezone.now() + timezone.timedelta(days=1)
    booking = Booking.objects.create(
        user=request.user,
        accommodation=accommodation,
        commission=commission,
        expiration_time=expiration_time
    )

    # Redirect to a success page or handle further actions
    return redirect('booking_success')


# @login_required
def booking_success(request):
    return render(request, 'booking_success.html')


def about(request):
    return render(request, 'about.html')
