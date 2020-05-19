from rest_framework import serializers

from .models import Portfolio
from .models import Instrument

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('name', 'description')

class InstrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        fields = ('symbol', 'portfolio')

