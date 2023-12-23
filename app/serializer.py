from .models import FruitsModel
from rest_framework.serializers import ModelSerializer
class FruitsSerializer(ModelSerializer):
    class Meta:
        model = FruitsModel
        fields = '__all__'