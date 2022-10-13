from rest_framework.serializers import FileField, Serializer, IntegerField


class UploadExelSerializer(Serializer):
    file = FileField()
    article = IntegerField()

    class Meta:
        fields = ["file", "article"]
