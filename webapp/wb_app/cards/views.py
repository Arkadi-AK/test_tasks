from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cards.serializer import ArticleSerializer, FileExelSerializer
from cards.wb_parser import parser, xlsx_to_list


class CardArticleAPIList(APIView):
    serializer_class = ArticleSerializer

    def post(self, request):
        article_serializer = ArticleSerializer(data=request.data)
        article_serializer.is_valid(raise_exception=True)
        article = article_serializer.validated_data["article"]
        result = parser([article])
        return Response(result, status=status.HTTP_200_OK)


class CardFileAPIList(APIView):
    serializer_class = FileExelSerializer

    def post(self, request):
        article_serializer = FileExelSerializer(data=request.FILES)
        article_serializer.is_valid(raise_exception=True)
        list_of_articles = xlsx_to_list(request)
        result = parser(list_of_articles)
        return Response(result, status=status.HTTP_200_OK)
