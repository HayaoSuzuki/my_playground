from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("card/", include("card.urls")),
    path("admin/", admin.site.urls),
]
