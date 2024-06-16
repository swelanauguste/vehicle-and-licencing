from django.urls import path

from .views import InsuredDetailView, InsuredListView, InsurerListView

app_name = "insurers"


urlpatterns = [
    path("", InsurerListView.as_view(), name="insurer-list"),
    path("insured/", InsuredListView.as_view(), name="list"),
    path("detail/<int:pk>/", InsuredDetailView.as_view(), name="detail"),
]
