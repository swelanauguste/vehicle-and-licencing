from django.urls import path

from .views import OwnerDetailView, OwnerListView

app_name = "owners"
urlpatterns = [
    path("", OwnerListView.as_view(), name="list"),
    path("detail/<int:pk>/", OwnerDetailView.as_view(), name="detail"),
]
