from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from advertisement.api.serializers import AdvertisementSerializer
from advertisement.models import Advertisement


class AdvertisementViewSet(viewsets.ViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    def retrieve(self, request, pk):
        advertisement = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(advertisement)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(None, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
