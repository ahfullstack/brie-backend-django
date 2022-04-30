from rest_framework import serializers 
from .models import Status 

class StatusSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Status # tell django which model to use
        fields = ('id', 'name', 'description','symptoms')