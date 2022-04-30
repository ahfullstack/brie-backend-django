from rest_framework import generics
from .serializers import StatusSerializer
from .models import Status

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = StatusSerializer # tell django what serializer to use

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer