from django.urls import path

from .views import (
    TransactionInsuranceDetailView,
    TransactionInsuranceListView,
    TransactionLicenceDetailView,
    TransactionLicenceListView,
    TransactionVehicleDetailView,
    TransactionVehicleListView,
    TransactionView,
)

app_name = "transactions"


urlpatterns = [
    path("", TransactionView.as_view(), name="transactions"),
    path("insurance/", TransactionInsuranceListView.as_view(), name="insurance-list"),
    path(
        "insurance/detail/<int:pk>/",
        TransactionInsuranceDetailView.as_view(),
        name="insurance-detail",
    ),
    path("licence/", TransactionLicenceListView.as_view(), name="licence-list"),
    path(
        "licence/detail/<int:pk>/",
        TransactionLicenceDetailView.as_view(),
        name="licence-detail",
    ),
    path("vehicle/", TransactionVehicleListView.as_view(), name="vehicle-list"),
    path(
        "vehicle/detail/<int:pk>/",
        TransactionVehicleDetailView.as_view(),
        name="vehicle-detail",
    ),
]
