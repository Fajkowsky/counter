from models import Counter, Word
from rest_framework import serializers


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ('user', 'word', 'timestamp')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('name',)
