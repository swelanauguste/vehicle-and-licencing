from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Insured, Insurer


class InsurerListView(ListView):
    model = Insurer


class InsuredListView(ListView):
    model = Insured
    paginate_by = 25


class InsuredDetailView(DetailView):
    model = Insured
