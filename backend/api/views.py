import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
@api_view(['POST'])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status=400)
    # Get random Product object from DB
    """Get model data in a certain order"""
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # If data exists, pass it to serializer to get a clean JSON data stream
    # if instance:
        # data = ProductSerializer(instance).data
    # Return the serialized data as response
    # return Response(data) 