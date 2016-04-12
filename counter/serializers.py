from models import Counter
from rest_framework import serializers


class CounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counter
        fields = ('user', 'word', 'timestamp')
