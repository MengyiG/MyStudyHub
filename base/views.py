from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q, Count
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Message
from .forms import RoomForm, UserForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        # check if the username exists in the database
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        # login the user
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password is incorrect")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = UserCreationForm()

    if request.method == "POST":
        # we use form = UserCreationForm(request.POST) to create a form instance
        # that is bound to the POST data, add the data to the form
        form = UserCreationForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # save the form data to the database
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # login the user
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")
    return render(request, "base/login_register.html", {"form": form})


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))

    # Get all topics and annotate them with the number of rooms
    topics = Topic.objects.annotate(
        num_rooms=Count('room')).order_by('-num_rooms')

    # Delete topics with zero count
    zero_count_topics = topics.filter(num_rooms=0)
    zero_count_topics.delete()

    # Refresh topics queryset after deletion
    topics = Topic.objects.annotate(
        num_rooms=Count('room')).order_by('-num_rooms')

    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {"rooms": rooms, "topics": topics,
               "room_count": room_count, "room_messages": room_messages}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()

    participants = room.participants.all()

    if request.method == "POST":
        messages = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect("room", pk=room.id)

    context = {"room": room, "room_messages": room_messages,
               "participants": participants}
    # use the render function to create an HTTP response
    return render(request, "base/room.html", context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()

    context = {"user": user, "rooms": rooms,
               "room_messages": room_messages, "topics": topics}
    return render(request, "base/profile.html", context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, "base/room_form.html", context)


# the updateRoom view function will be used to update a room
# it will take a request and a pk parameter
# the pk parameter will be used to fetch the room from the database

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    # this form will be pre-populated with the data from the room instance
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse("You are not allowed here")

    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)
        # this is the form that will be used to update the room
        room.name = request.POST.get("name")
        room.topic = topic
        room.description = request.POST.get("description")
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, "base/room_form.html", context)


@login_required(login_url='login')
def deteleRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here")

    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, "base/delete.html", {'obj': 'room'})


@login_required(login_url='login')
def deteleMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed here")

    if request.method == "POST":
        message.delete()
        return redirect('home')
    return render(request, "base/delete.html", {'obj': 'message'})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=request.user)

    if request.method == "POST":
        # we use form = UserForm(request.POST, instance=user) to create a form instance
        # that is bound to the POST data, add the data to the form
        # and tell which user instance to update
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, "base/update-user.html", {'form': form})
