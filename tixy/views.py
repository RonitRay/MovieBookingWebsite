from .models import Movie, Schedule, Slot, Booking
from django.shortcuts import render,redirect, get_object_or_404

def index(request):
    all_movies= Movie.objects.all()
    context = {'all_movies': all_movies,}
    return render(request, 'tixy/index.html', context)


def detail(request, movie_id):
    booking = Booking.objects.all()
    movie = get_object_or_404(Movie, id=movie_id)

    return render(request, 'tixy/detail.html', {'booking': booking,'movie': movie, 'all_shows': Schedule.objects.all(),})


def book(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id)
    seat = Booking(slot=slot)
    seat.save()

    return redirect('../../../admin/tixy/booking/' + str(seat.id) + '/change/', {'slot': slot})