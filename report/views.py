from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .missing_report import ReportListMixin, ReportDetailMixin

# Create your views here.

class ReportList(ReportListMixin, ListView):
    ''' List view for Missing people report '''
    template_name = "report/report.html"
    context_object_name = "reports"


class ReportDetails(ReportDetailMixin, DetailView):
    ''' Details view for Missing people report '''
    template_name = "report/report_detaill.html"
    context_object_name = "report" 
