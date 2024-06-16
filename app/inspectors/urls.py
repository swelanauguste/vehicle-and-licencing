from django.urls import path

from .views import InspectorListView

app_name = "inspector"

urlpatterns = [
    path("", InspectorListView.as_view(), name="list"),
]
