from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import FruitsModel
from .serializer import FruitsSerializer
class FruitsViewset(ModelViewSet):
    queryset = FruitsModel.objects.all()
    serializer_class = FruitsSerializer