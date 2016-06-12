from rest_framework import serializers
from .models import *


class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = ('id', 'when', 'rating', 'duration')
