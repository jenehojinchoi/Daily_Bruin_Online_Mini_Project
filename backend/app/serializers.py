from rest_framework import serializers
from .models import Organization, Source

class OrganizationSerializer(serializers.ModelSerializer):
    sources = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    class Meta:
        model = Organization
        fields = ['name', 'notes', 'sources']

class SourceSerializer(serializers.ModelSerializer):
    organization = serializers.SlugRelatedField(
        many=False, 
        read_only=True, 
        slug_field='name'
    )
    class Meta:
        model = Source
        fields = ['name', 'organization', 'email', 'notes', 'phone']
        related_object = 'organization'