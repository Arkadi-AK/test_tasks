from django.core.validators import FileExtensionValidator
from rest_framework.serializers import FileField, Serializer, IntegerField


class ArticleSerializer(Serializer):
    article = IntegerField()

    class Meta:
        fields = ["article"]


class FileExelSerializer(Serializer):
    file = FileField(validators=[FileExtensionValidator(allowed_extensions=["xlsx"])])

    class Meta:
        fields = ["file"]
