from rest_framework.views import APIView
from rest_framework import serializers, viewsets

from searches.models import Search


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    http_method_names = ['get']
