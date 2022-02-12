from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .serializers import SourceSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from app.models import Source

@api_view(['GET'])
def getSources(request):
    sources = Source.objects.all()
    serializer = SourceSerializer(sources, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getSource(request, id):
    source = get_object_or_404(
        Source,
        id=id,
    )
    serializer = SourceSerializer(source, many=False)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def updateSource(request, id):
    source = get_object_or_404(
        Source,
        id=id,
    )
    serializer = SourceSerializer(source, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'id': source.id})
    else:
        return JsonResponse(serializer.errors)

@api_view(['POST'])
def createSource(request):
    data = request.data

    try: 
        print(data)
        source = Source.objects.create(
            name = data['name'],
            organization = data['organization'],
            email = data['email'],
            notes = data['notes'],
            phone = data['phone'],
        )
        print(source)
        return Response("Successfully created")
        
    except: 
        message = {'detail': 'This source already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteSource(request, id):
	source = get_object_or_404(
		Source,
		id=id
	)
	source.delete()
	return JsonResponse({
		'id': id
	})

