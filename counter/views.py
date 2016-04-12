from models import Counter, Word, User
from rest_framework import viewsets
from serializers import CounterSerializer, WordSerializer, UserSerializer


class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all().order_by('-timestamp')
    serializer_class = CounterSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
