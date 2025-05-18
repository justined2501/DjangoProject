from __future__ import annotations

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from auto.models import Auto, Brand


class AutoListView(ListView):
    model = Auto
    template_name = 'auto/list.html'
    context_object_name = 'auto'
    paginate_by = 5

    def get_ordering(self) -> str | None:
        sort = self.request.GET.get('sort', self.ordering)
        sort_dict = {
            "cheap": "cost",
            "expensive": "-cost",
            "novelty": "-created_at",
            "title": "brand",
            "-title": "-brand",
            "year": "year_of_release",
            "-year": "-year_of_release",
        }
        if sort:
            return sort_dict.get(sort)



    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        brand = Brand.objects.all()
        data['brand'] = brand
        return data


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
        brand_id = self.request.GET.get('brand')
        if model:
            queryset = queryset.filter(model=model)
        if model:
            queryset = queryset.filter(model__iexact=model)
        if brand_id:
            brand_name = Brand.objects.get(id=brand_id).name
            queryset = queryset.filter(brand__iexact=brand_name)
        return queryset
