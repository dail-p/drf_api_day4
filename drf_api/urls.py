from django.contrib import admin
from django.urls import path, include

from api.urls import router as api_router

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(api_router.urls))
]
