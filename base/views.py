from django.shortcuts import render
from .models import Room

# rooms = [
#     {"id": 1, "name": "Let's learn Python"},
#     {"id": 2, "name": "Designing a Django app"},
#     {"id": 3, "name": "Frontend development"},
# ]


def home(request):
    # variable that holds response = model name.model objects attributes
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    # use the render function to create an HTTP response
    # containing the template home.html
    # and pass the rooms variable to the template

    # The purpose of this code is to handle an HTTP request
    # fetch the appropriate template ("home.html"), and render it with the provided context data.
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    # create a context dictionary with the room variable
    # and pass it to the room template
    # the template will be able to access the room variable
    context = {"room": room}
    # use the render function to create an HTTP response
    return render(request, "base/room.html", context)
