from django.urls import path
from .views import *
urlpatterns = [
path('', RegionListCreateView.as_view()),
path('', RegionDetailView.as_view()),
path('', SalespeopleListCreateView.as_view()),
path('', SalespeopleDetailView.as_view()),
path('', SaleListCreateView.as_view()),
path('', SaleDetailView.as_view()),
path('', CommissionRateListCreateView.as_view()),
path('', CommissionRateDetailView.as_view()),
path('', UseListCreateView.as_view()),
path('', UseDetailView.as_view()),
path('calculate-commissions/', calculate_commissions, name='calculate_commissions'),
path('calculate-commissions/<int:salesperson_id>/<int:month>/<int:year>/', calculate_commissions,
         name='calculate_commissions'),

]