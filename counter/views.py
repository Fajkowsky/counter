from models import Counter
from rest_framework import viewsets
from serializers import CounterSerializer


class CounterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Counter.objects.all().order_by('-timestamp')
    serializer_class = CounterSerializer
