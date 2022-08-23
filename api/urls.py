from django.contrib import admin
from django.urls import path, include, re_path

from core.router import router as core_router
from eBook.router import router as ebook_router

from .yasg import swaggerurlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_router.urls)),
    path('', include(ebook_router.urls)),
]

urlpatterns += swaggerurlpatterns
