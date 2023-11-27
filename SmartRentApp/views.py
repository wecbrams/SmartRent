from django.shortcuts import render


# Create your views here.


def register(request):
    # if request.method == "POST":

    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def reset(request):
    return render(request, 'reset.html')


def index(request):
    return render(request, 'index.html')


def accommodations(request):
    return render(request, 'accommodation.html')
