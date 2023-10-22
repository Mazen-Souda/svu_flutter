# regions/views.py
from rest_framework import generics
from .models import Region, Salespeople, Sale, CommissionRate, Use
from .api.serializers import RegionSerializer, SalespeopleSerializer, SaleSerializer, CommissionRateSerializer, \
    UseSerializer ,CommissionCalculationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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




# Create a new view that will handle the commissions calculation and display the information. In this view, you will perform the following steps:
#
# a. Accept the salesperson's ID and month/year as input.
# b. Retrieve the sales records for the given salesperson and period.
# c. Calculate commissions for each region based on the rules and the assigned region.
# d. Display the required information in your interface.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate_commissions(request):
    try:
        # Retrieve parameters from the request, e.g., salesperson_id, month, and year.
        salesperson_id = request.GET.get('salesperson_id')
        month = int(request.GET.get('month'))
        year = int(request.GET.get('year'))

        # Retrieve the salesperson and assigned region.
        salesperson = Salespeople.objects.get(pk=salesperson_id)
        assigned_region = salesperson.assigned_region

        # Retrieve sales records for the given salesperson and period.
        sales_records = Sale.objects.filter(
            salesperson=salesperson, date__month=month, date__year=year
        )

        # Calculate commissions for each region based on the rules.
        commissions = {}
        for region in Region.objects.all():
            in_region_rate = CommissionRate.objects.get(
                sales_amount_limit=1000000, region=region
            ).in_region_rate
            out_region_rate = CommissionRate.objects.get(
                sales_amount_limit=1000000, region=region
            ).out_region_rate
            total_sales_in_region = sum(
                record.amount for record in sales_records.filter(region=region)
            )
            total_sales_out_region = sum(
                record.amount for record in sales_records.exclude(region=region)
            )

            if region == assigned_region:
                commission = (
                    min(total_sales_in_region, 1000000) * in_region_rate
                ) + (max(0, total_sales_in_region - 1000000) * 0.07)
            else:
                commission = (
                    min(total_sales_out_region, 1000000) * out_region_rate
                ) + (max(0, total_sales_out_region - 1000000) * 0.04)

            commissions[region.region_name] = commission

        # Create a serializer instance and return the data as JSON
        serializer = CommissionCalculationSerializer({
            'salesperson_name': salesperson.name,
            'month': month,
            'year': year,
            'commissions': commissions,
        })

        return Response(serializer.data)

    except Exception as e:
        # Handle errors and missing data here
        return Response({'error_message': str(e)}, status=400)