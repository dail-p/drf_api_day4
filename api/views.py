from django.db.models import F
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from api.models import Author, Book
from api.serializer import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    parser_classes = (JSONParser,)


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    parser_classes = (JSONParser,)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LibraryView(BookViewSet):
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = super().get_queryset()
        filter = dict(self.request.query_params)
        page = filter.pop('page', None)
        for key, item in filter.items():
            if key == 'authors__name':
                qs = qs.filter(authors__name__in=item)
            if key == 'title':
                qs = qs.filter(title__in=item)
        return qs
