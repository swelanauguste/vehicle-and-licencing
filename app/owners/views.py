from django.db import models
from django.db.models import F, Q, Value
from django.db.models.functions import Concat
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView
from vehicles.models import Vehicle

from .models import Owner


class OwnerListView(ListView):
    model = Owner
    paginate_by = 25

    def get_queryset(self):
        queryset = Owner.objects.all().order_by("last_name", "first_name")
        query = self.request.GET.get("q")

        if query:
            queryset = (
                Owner.objects.annotate(
                    full_name=Concat(
                        F("last_name"),
                        Value(" "),
                        F("first_name"),
                        output_field=models.CharField(),
                    )
                )
                .filter(
                    Q(full_name__icontains=query.replace("-", "").replace(",", ""))
                    | Q(nis__icontains=query)
                    | Q(driver_number__icontains=query)
                    | Q(driver_code__icontains=query)
                    | Q(address__icontains=query)
                    | Q(location_code__icontains=query)
                    | Q(nationality__icontains=query)
                    | Q(gender__gender__icontains=query)
                )
                .distinct()
                .order_by("last_name", "first_name")
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner_count"] = Owner.objects.all().count()
        return context


class OwnerDetailView(DetailView):
    model = Owner
