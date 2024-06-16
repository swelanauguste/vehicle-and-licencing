from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Vehicle


class VehicleListView(ListView):
    model = Vehicle
    paginate_by = 25

    def get_queryset(self):
        queryset = Vehicle.objects.all().order_by("licence_number")
        query = self.request.GET.get("q")

        if query:
            return (
                Vehicle.objects.filter(
                    Q(owners__last_name__icontains=query)
                    | Q(owners__first_name__icontains=query)
                    | Q(owners__driver_number__icontains=query)
                    | Q(owners__driver_code__icontains=query)
                    | Q(licence_number__icontains=query)
                    | Q(reg_on__icontains=query)
                    | Q(number__icontains=query)
                    | Q(manufacturer__manufacturer__icontains=query)
                    | Q(chassis_number__icontains=query)
                    | Q(engine_number__icontains=query)
                )
                .distinct()
                .order_by("licence_number")
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle_count"] = Vehicle.objects.all().count()
        return context


class VehicleDetailView(DetailView):
    model = Vehicle
