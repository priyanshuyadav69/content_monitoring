from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

from .models import Keyword, Flag
from .serializers import KeywordSerializer, FlagSerializer
from .services import run_scan


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class FlagViewSet(viewsets.ModelViewSet):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        status_value = request.data.get('status')

        if status_value:
            instance.status = status_value
            instance.reviewed_at = timezone.now()
            instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@api_view(['POST'])
def scan_view(request):
    run_scan()
    return Response({"message": "Scan completed"})