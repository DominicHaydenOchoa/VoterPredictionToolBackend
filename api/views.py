from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import testing_data_raw
from .serializers import testing_data_raw_serializer

# Create your views here.
def testing_data_raw_list(request):

    if request.method == 'GET':
        data = testing_data_raw.objects.all()
        serializer = testing_data_raw_serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = testing_data_raw_serializer(data=data)

        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)