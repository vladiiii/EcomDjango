from django.contrib import admin
from django.urls import path

from core.views import front_page, about

urlpatterns = [
    path("", front_page, name="frontpage"),
    path("about/", about, name="about"),
    path("admin/", admin.site.urls),
]
