from rest_framework.routers import DefaultRouter

from api.views import AuthorViewSet, BookViewSet, LibraryView

app_name = 'api'

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'library', LibraryView, basename='library')