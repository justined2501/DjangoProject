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
            if paginate in [5,10,25,50]:
                return paginate
            else:
                return self.paginate_by
        except(ValueError, TypeError):
            return self.paginate_by


