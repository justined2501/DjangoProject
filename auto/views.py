from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from auto.models import Auto


class AutoListView(ListView):
    model = Auto
    template_name = 'auto/list.html'
    context_object_name = 'auto'
    paginate_by = 1

    def get_ordering(self) -> str | None:
        sort = self.request.GET.get('sort', self.ordering)
        sort_dict = {
            "cheap": "cost",
            "expensive": "-cost",
            "novelty": "-created_at",
            "title": "title",
            "-title": "-title",
        }
        if sort:
            return sort_dict.get(sort)

    def get_paginate_by(self, queryset):
        try:
            paginate = int(self.request.GET.get('limit', self.paginate_by))
            if paginate in [5, 10, 25, 50]:
                return paginate
            else:
                return self.paginate_by
        except (ValueError, TypeError):
            return self.paginate_by

    def get_queryset(self):
        queryset = super().get_queryset()
        model = self.request.GET.get('model')
        if model is None:
            return queryset
        return queryset.filter(model__startswith=model)