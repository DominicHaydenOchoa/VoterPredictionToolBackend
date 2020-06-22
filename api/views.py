from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import testing_data_raw, training_data_raw, testing_data_input
from .serializers import testing_data_raw_serializer, training_data_raw_serializer, testing_data_input_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def testing_data_raw_list(request):

    if request.method == 'GET':
        data = testing_data_raw.objects.all()
        serializer = testing_data_raw_serializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = testing_data_raw_serializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def testing_data_input_list(request):

    if request.method == 'GET':
        data = testing_data_input.objects.all()
        serializer = testing_data_input_serializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print(request.data)
        serializer = testing_data_input_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def testing_data_input_detail(request, user_id):

    try:
        data = testing_data_input.objects.get(user_id=user_id)
    except: 
        testing_data_input.DoesNotExist(status=404)

    if request.method == 'GET':
        serializer = testing_data_input_serializer(data) 
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = training_data_input_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def training_data_raw_list(request):

    if request.method == 'GET':
        data = training_data_raw.objects.all()
        serializer = training_data_raw_serializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = testing_data_raw_serializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def testing_data_raw_detail(request, pk):
    try:
        data = testing_data_raw.objects.get(pk=pk)
    except: 
        testing_data_raw.DoesNotExist(status=404)

    if request.method == 'GET':
        serializer = testing_data_raw_serializer(data) 
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = training_data_raw_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=204)