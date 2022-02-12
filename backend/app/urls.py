from django.urls import path
from app.views import getSources, getSource, createSource, updateSource, deleteSource

urlpatterns = [
    path('source/', getSources, name="sources"),
    path('source/<int:id>/', getSource, name="source"), 
    path('source/create/', createSource, name="create"), 
    path('source/update/<int:id>/', updateSource, name="update"), 
    path('source/delete/<int:id>/', deleteSource, name="delete"), 
]
