from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import Http404
from .models import MissingReport

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

class ReportListMixin(object):
    ''' Render list of missing people from cache or db '''
    model = MissingReport

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            if cache.get(q):
                reports = cache.get(q)
                print("Result from cache")
            else:
                reports = self.model.objects.filter(name__icontains=q)
                cache.set(q, reports, timeout=CACHE_TTL) 
                print("Result from DB")
        else:
            if cache.get("missing_person_list"):
                reports = cache.get("missing_person_list")
                print("Result from cache")
            else:
                reports = self.model.objects.all()
                cache.set("missing_person_list", reports, timeout=CACHE_TTL)
                print("Result from DB")

        return reports

class ReportDetailMixin(object):
    ''' Render single obj of missing people from cache or db '''
    model = MissingReport

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if cache.get(f"report_{pk}"):
            obj = cache.get(f"report_{pk}")
            print("Result from cach")
        else:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                obj = queryset.get(pk=pk)
                cache.set(f"report_{pk}", obj, timeout=CACHE_TTL)
                print("Result from DB")
            except queryset.model.DoesNotExist:
                raise Http404(_("No %(verbose_name)s found matching the query") %
                            {'verbose_name': queryset.model._meta.verbose_name})
        return obj
        