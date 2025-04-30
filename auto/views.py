from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from auto.models import Auto


class AutoListView(ListView):
    model = Auto
    template_name = 'auto/list.html'
    context_object_name = 'auto'
    paginate_by = 5

    def get_paginate_by(self, queryset):
        try:
            paginate = int(self.request.GET.get('paginate_by', self.paginate_by))
            if 51 > paginate > 1:
                return paginate
        except(ValueError, TypeError):
            pass
        return self.paginate_by

