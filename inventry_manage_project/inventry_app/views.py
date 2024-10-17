from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from .models import Item, User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ItemSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpResponse
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import json
# Create your views here.

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': 'api/items'
    }
    return Response(api_urls)

class ReadItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    # def get(self, request, *args, **kwargs):
    #     item_id = kwargs["pk"]
    #     if cache.get(item_id):
    #         recipe = cache.get(item_id)
    #         print("DATA COMING FROM CACHE")
    #     else:
    #         try:
    #             recipe = Item.objects.get(id = item_id)
    #             cache.set(item_id , recipe)
    #             print("DATA COMING FROM DB")
    #             # data = serializers.serialize("xml", recipe)
    #             # print(data, '-------------')
    #             context = {'id' : recipe.id}
    #             return HttpResponse(json.dumps(context))
    #         except Item.DoesNotExist:
    #             return HttpResponse('Item does not exist')

class UpdateItem(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CreateItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class DeleteItem(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ReadItemByID(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "pk"
    
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer