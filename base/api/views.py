from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


# the getRoutes function will return a list of all the available routes in the API
@api_view(['GET'])
def getRoutes(requests):
    routes = [
        'GET /api',
        'GET /api/rooms/',
        'GET /api/rooms/:id/',

    ]

    return Response(routes)


# the getRooms function will return a list of all the rooms in the database
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # The RoomSerializer class is used to serialize the rooms
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
