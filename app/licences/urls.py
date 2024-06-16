from django.urls import path

from .views import (
    LicenceDetailView,
    LicenceListView,
    LicenceTypeDetailView,
    LicenceTypeListView,
)

app_name = "licences"


urlpatterns = [
    path("", LicenceTypeListView.as_view(), name="list-type"),
    path("detail/type/<int:pk>/", LicenceTypeDetailView.as_view(), name="detail-type"),
    path("licences/", LicenceListView.as_view(), name="list"),
    path("licence/detail/<int:pk>/", LicenceDetailView.as_view(), name="detail"),
]
