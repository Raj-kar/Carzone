from contacts.models import Contact
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):

    if request.method == "POST":
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        customer_need = request.POST["customer_need"]
        city = request.POST["city"]
        state = request.POST["state"]
        phone_number = request.POST["phone"]
        message = request.POST["message"]

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry about this car. Please wait until we get back to you')
                return redirect(f'/cars/{car_id}')

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name,
                          email=email, customer_need=customer_need, city=city, state=state, phone_number=phone_number, message=message)
        
        admin_email = User.objects.get(is_superuser=True)
        send_mail(
            subject="New Car Inquiry",
            message=f'You\'ve a new inquiry for the car {car_title}. Please login to your admin panel for more info.',
            from_email="rajwithcode@gmail.com",
            recipient_list=[admin_email.email],
            fail_silently=False
        )
        contact.save()
        messages.success(
            request, 'Your request has been submitted, we will get back to you shortly !')
        return redirect(f'/cars/{car_id}')
