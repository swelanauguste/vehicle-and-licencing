from django.urls import path

from .views import VehicleDetailView, VehicleListView

app_name = "vehicles"


urlpatterns = [
    path("", VehicleListView.as_view(), name="list"),
    path("detail/<int:pk>/", VehicleDetailView.as_view(), name="detail"),
]
