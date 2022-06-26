from rest_framework.response import Response
from rest_framework.decorators import api_view   #as a decorator
from baseApp.models import *
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    person = {'name':'sow','age':27}
    return Response(person)     #op will be json data

@api_view(['GET'])
def getValues(req):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True) #many-will serialize many items and convert it to one
    return Response(serializer.data)

# To create/post details from front end
@api_view(['POST'])
def addValues(req):
    serializer = ItemSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)