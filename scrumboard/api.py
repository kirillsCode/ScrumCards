from rest_framework.viewsets import ModelViewSet

from .models import Card, List

from .serializers import ListSerializer, CardSerializer


class ListViewSet(ModelViewSet):

    # nested query to display only lists which have cards with business value more then 10
    _query = "select * from scrumboard_list where id in (" \
             "select list_id from scrumboard_card where business_values > 10);"
    queryset = List.objects.raw(_query)
    serializer_class = ListSerializer


class CardViewSet(ModelViewSet):
    _query = "select title, description from scrumboard_card;"
    queryset = Card.objects.raw(_query)
    serializer_class = CardSerializer



