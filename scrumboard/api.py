from rest_framework.generics import ListAPIView

from .models import Card, List

from .serializers import ListSerializer, CardSerializer


class ListApi(ListAPIView):

    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardApi(ListAPIView):

    queryset = Card.objects.all()
    serializer_class = CardSerializer



