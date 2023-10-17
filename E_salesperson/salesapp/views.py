# regions/views.py
from rest_framework import generics
from .models import Region, Salespeople, Sale, CommissionRate, Use
from .api.serializers import RegionSerializer,SalespeopleSerializer,SaleSerializer,CommissionRateSerializer,UseSerializer

class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class SalespeopleListCreateView(generics.ListCreateAPIView):
    queryset = Salespeople.objects.all()
    serializer_class = SalespeopleSerializer

class SalespeopleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salespeople.objects.all()
    serializer_class = SalespeopleSerializer



class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CommissionRateListCreateView(generics.ListCreateAPIView):
    queryset = CommissionRate.objects.all()
    serializer_class = CommissionRateSerializer

class CommissionRateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommissionRate.objects.all()
    serializer_class = CommissionRateSerializer


class UseListCreateView(generics.ListCreateAPIView):
    queryset = Use.objects.all()
    serializer_class = UseSerializer

class UseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Use.objects.all()
    serializer_class = UseSerializer