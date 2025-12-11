from rest_framework import serializers
from .models import Train

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id','name','fare','total_seats','available_seats']
