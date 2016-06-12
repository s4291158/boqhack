from rest_framework import viewsets
from .serializer import *


class RecordingViewSet(viewsets.ModelViewSet):
    # Viewset provides 'list', 'create', 'retreieve', 'update', and 'destroy' actions
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
