from django.contrib import admin
from django.urls import path, include

from core.views import front_page, about

urlpatterns = [
    path("about/", about, name="about"),
    path("admin/", admin.site.urls),
    path("", include("store.urls")),
    path("", front_page, name="frontpage"),
]
