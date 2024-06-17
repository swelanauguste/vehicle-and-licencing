from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import TransactionInsurance, TransactionLicence, TransactionVehicle


class TransactionView(TemplateView):
    template_name = "transactions/transactions.html"


class TransactionLicenceListView(ListView):
    model = TransactionLicence
    paginate_by = 25


class TransactionLicenceDetailView(DetailView):
    model = TransactionLicence


class TransactionVehicleListView(ListView):
    model = TransactionVehicle
    paginate_by = 25


class TransactionVehicleDetailView(DetailView):
    model = TransactionVehicle


class TransactionInsuranceListView(ListView):
    model = TransactionInsurance
    paginate_by = 25


class TransactionInsuranceDetailView(DetailView):
    model = TransactionInsurance
