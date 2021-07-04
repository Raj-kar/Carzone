from django.contrib import messages
from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('created_at').filter(is_featured=True)
    all_cars = Car.objects.order_by('created_at').all()
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, "pages/home.html", data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, "pages/about.html", data)


def services(request):
    return render(request, "pages/services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        admin_email = User.objects.get(is_superuser=True)
        msg_body = f'''
            Name = {name} \n
            email = {email} \n
            phone = {phone} \n
            message = {message}
        '''
        try:
            send_mail(
                subject=subject,
                message=msg_body,
                from_email="rajwithcode@gmail.com",
                recipient_list=[admin_email.email],
                fail_silently=False
            )
            messages.success(
                request, 'We got your email, we\'ll contact with you soon !')
        except Exception as e:
            messages.error(
                request, 'Something went Wrong ! Please try again .')
            print(e)

    return render(request, "pages/contact.html")
