from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PortfolioSerializer
from .serializers import InstrumentSerializer

from .models import Portfolio
from .models import Instrument

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by('name')
    serializer_class = PortfolioSerializer

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all().order_by('symbol')
    serializer_class = InstrumentSerializer