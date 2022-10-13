from rest_framework import serializers
from rest_framework.serializers import FileField, Serializer, IntegerField

from cards.pydantic_json import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class UploadExelSerializer(Serializer):
    file = FileField()
    article = IntegerField()

    class Meta:
        fields = ["file", "article"]
