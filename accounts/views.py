from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from cars.models import Car
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You're now logged in !")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Login credentials !")
            return redirect('login')
    if not request.user.is_authenticated:
        return render(request, "accounts/login.html")
    return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exits !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exits !')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(
                        request, "You are now logged in !")
                    user.save()
                    return redirect('dashboard')
        else:
            messages.error(request, 'Password mismatch !')
            return redirect('register')
    if not request.user.is_authenticated:
        return render(request, "accounts/register.html")
    return redirect('dashboard')


@login_required(login_url='/accounts/login')
def dashboard(request):
    inquired_cars = Contact.objects.order_by('create_date').filter(user_id = request.user.id).all()
    

    return render(
        request, "accounts/dashboard.html", 
        {'cars': inquired_cars}
    )


def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect('home')
