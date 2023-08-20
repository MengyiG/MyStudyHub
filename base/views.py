from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

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


def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        # we use form = RoomForm(request.POST) to create a form instance
        # that is bound to the POST data, add the data to the form
        form = RoomForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # save the form data to the database
            form.save()
            # redirect the user to the home page
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)


# the updateRoom view function will be used to update a room
# it will take a request and a pk parameter
# the pk parameter will be used to fetch the room from the database


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    # this form will be pre-populated with the data from the room instance
    form = RoomForm(instance=room)

    if request.method == "POST":
        # we use form = RoomForm(request.POST, instance=room) to create a form instance
        # that is bound to the POST data, add the data to the form
        # and tell which room instance to update
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, "base/room_form.html", context)
