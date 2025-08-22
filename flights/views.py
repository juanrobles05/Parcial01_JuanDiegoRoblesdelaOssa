from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .models import Flight
from .forms import FlightForm

def home(request):
    return render(request, 'flights/home.html')

def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flights:list')
    else:
        form = FlightForm()
    return render(request, 'flights/form.html', {'form': form})

def list_flights(request):
    flights = Flight.objects.all()
    return render(request, 'flights/list.html', {'flights': flights})

def flight_stats(request):
    counts = Flight.objects.values('flight_type').annotate(total=Count('id'))
    by_type = {row['flight_type']: row['total'] for row in counts}
    n_national = by_type.get(Flight.NATIONAL, 0)
    n_international = by_type.get(Flight.INTERNATIONAL, 0)

    avg_national = (Flight.objects
                    .filter(flight_type=Flight.NATIONAL)
                    .aggregate(avg=Avg('price'))['avg'])

    return render(request, 'flights/stats.html', {
        'n_national': n_national,
        'n_international': n_international,
        'avg_national': avg_national,
    })