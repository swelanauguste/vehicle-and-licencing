from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Inspector


class InspectorListView(ListView):
    model = Inspector

    def get_queryset(self):
        queryset = Inspector.objects.all()
        query = self.request.GET.get("q")

        if query:
            return (
                Inspector.objects.filter(Q(inspector__icontains=query))
                .distinct()
                .order_by("inspector")
            )
        return queryset

    extra_context = {"inspector_count": Inspector.objects.all().count()}
