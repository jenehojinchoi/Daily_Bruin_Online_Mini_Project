from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .serializers import SourceSerializer, OrganizationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from app.models import Organization, Source


# organization
@api_view(['GET'])
def getOrganizations(request):
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def getOrganization(request, id):
    organization = get_object_or_404(
        Organization,
        id=id,
    )
    serializer = OrganizationSerializer(organization, many=False)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def createOrganization(request):
    data = request.data

    try: 
        if Organization.objects.filter(name = data['name']).exists():
            message = {'detail': 'Organization with this name already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        organization = Organization.objects.create(
            name = data['name'],
            notes = data['notes'],
        )
        return Response("Successfully created")
        
    except: 
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# sources
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
        if Source.objects.filter(name = data['name']).exists():
            message = {'detail': 'Source with this name already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
        if Source.objects.filter(email = data['email']).exists():
            message = {'detail': 'Source with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        else: 
            source = Source.objects.create(
                name = data['name'],
                organization_id = data['organization'],
                email = data['email'],
                notes = data['notes'],
                phone = data['phone'],
            )
            return Response("Successfully created")
        
    except: 
        message = {'detail': 'This source cannot be created'}
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