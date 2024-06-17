from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("owners.urls", namespace="owners")),
    path("inspectors/", include("inspectors.urls", namespace="inspectors")),
    path("insurers/", include("insurers.urls", namespace="insurers")),
    path("licences/", include("licences.urls", namespace="licences")),
    path("vehicles/", include("vehicles.urls", namespace="vehicles")),
    path("transactions/", include("transactions.urls", namespace="transactions")),
]
