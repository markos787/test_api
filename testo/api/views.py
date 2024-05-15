from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import zasadzki
from .serializers import zasadzkiSerializer
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# class zasadzkiListCreate(generics.ListCreateAPIView):
#     queryset=zasadzki.objects.all()
#     serializer_class=zasadzkiSerializer

#     def delete(self, request, *args, **kwargs):
#         zasadzki.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def select_related(self, request, *args, **kwargs):
#         zasadzki.objects.all().select_related()
#         return Response(status=status.HTTP_302_FOUND)

def filter_zasadzki(queryset, request):
    search_filter = SearchFilter()
    filter_backend = DjangoFilterBackend()
    
    # Apply search filter
    queryset = search_filter.filter_queryset(request, queryset, view=None)
    # Apply filter backend
    queryset = filter_backend.filter_queryset(request, queryset, view=None)
    
    return queryset

class zasadzkiSearchView(generics.ListAPIView):
    queryset=zasadzki.objects.all()
    serializer_class=zasadzkiSerializer
    filter_backends=[SearchFilter, DjangoFilterBackend]
    search_fields=['typ']

    def get_queryset(self):
        queryset = super().get_queryset()
        return filter_zasadzki(queryset, self.request)

class zasadzkiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=zasadzki.objects.all()
    serializer_class=zasadzkiSerializer
    lookup_field='pk'
    
class zasadzkiView(APIView):
    def get(self, request, format=None):
        queryset = zasadzki.objects.all()
        id_param = request.GET.get('id', None)
        if id_param is not None and id_param != '':
            queryset = queryset.filter(id=id_param)
        serializer = zasadzkiSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def zasadzki_table(request):
    return render(request, 'table.html')
    