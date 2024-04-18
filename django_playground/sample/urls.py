from django.urls import path

from .views import CardCreateView, CardListView

app_name = "sample"
urlpatterns = [
    path("", CardListView.as_view(), name="list"),
    path("create/", CardCreateView.as_view(), name="create"),
]
