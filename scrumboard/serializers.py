from rest_framework import serializers

from .models import List, Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:

        model = Card
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):

    #cards = serializers.RelatedField(many=True, read_only=True)
    cards = CardSerializer(many=True, read_only=True)

    class Meta:

        model = List
        fields = '__all__'


