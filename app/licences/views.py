from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Licence, LicenceType


class LicenceTypeListView(ListView):
    model = LicenceType


class LicenceTypeDetailView(DetailView):
    model = LicenceType


class LicenceListView(ListView):
    model = Licence
    paginate_by = 25


class LicenceDetailView(DetailView):
    model = Licence
