from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from cars.models import Car


# Create your views here.
def cars(request):
    cars = Car.objects.order_by("created_at")
    paginator = Paginator(cars, 4) # 4 car per page
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    # search data
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }

    return render(request, "cars/cars.html", data)


def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, "cars/car_detail.html", {'car': car})


def search(request):
    search_cars = Car.objects.order_by("created_at")
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    condition_search = Car.objects.values_list('condition', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars = search_cars.filter(description__icontains = keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            search_cars = search_cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            search_cars = search_cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            search_cars = search_cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            search_cars = search_cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            search_cars = search_cars.filter(price__gte=min_price, price__lte=max_price)

    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            search_cars = search_cars.filter(condition__iexact=condition)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            search_cars = search_cars.filter(transmission__iexact=transmission)

    data = {
        'search_cars': search_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'condition_search': condition_search,
        'transmission_search': transmission_search
    }

    return render(request, "cars/search.html", data)
