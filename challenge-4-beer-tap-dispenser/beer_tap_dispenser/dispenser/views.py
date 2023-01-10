from django.shortcuts import render
from .models import Dispenser, Usage
from .serializers import DispenserSerializer, UsageSerializer, DispenserStatusSerializer, DispenserSerializerCreation
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

class DispenserCreate(generics.CreateAPIView):
    queryset = Dispenser.objects.all()
    serializer_class = DispenserSerializerCreation

class DispenserUpdate(APIView):
    def get_object(self, unique_id):
        try:
            return Dispenser.objects.get(unique_id=unique_id)
        except Dispenser.DoesNotExist:
            raise Http404

    def put(self, request, unique_id, format=None):
        dispenser = self.get_object(unique_id)
        serializer = DispenserStatusSerializer(dispenser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class DisperserRetrieve(generics.RetrieveAPIView):
    queryset = Dispenser.objects.all()
    serializer_class = DispenserSerializer
    lookup_field = 'unique_id'