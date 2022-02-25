from django.urls import path
from app.views import (
    getSources, getSource, createSource, updateSource, deleteSource, 
    getOrganizations, getOrganization, createOrganization, updateOrganization, deleteOrganization
)

urlpatterns = [
    # sources
    path('source/', getSources, name="sources"),
    path('source/<int:id>/', getSource, name="source"), 
    path('source/create/', createSource, name="create"), 
    path('source/update/<int:id>/', updateSource, name="update"), 
    path('source/delete/<int:id>/', deleteSource, name="delete"), 

    # organizations
    path('organization/', getOrganizations, name="organizations"),path('organization/<int:id>/', getOrganization, name="organization"), 
    path('organization/create/', createOrganization, name="create-organization"), 
    path('organization/update/<int:id>/', updateOrganization, name="update-organization"), 
    path('organization/delete/<int:id>/', deleteOrganization, name="delete-organization"),
]
