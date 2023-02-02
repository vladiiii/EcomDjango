from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import front_page, about

urlpatterns = [
    path("about/", about, name="about"),
    path("admin/", admin.site.urls),
    path("", include("store.urls")),
    path("", front_page, name="frontpage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
