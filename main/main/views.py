from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView
from worker.models import Auto, Sales


class WelcomePageView(ListView):
    model = Auto
    template_name = 'main/welcomepage.html'
    context_object_name = 'auto'

def sell_auto(request, pk: int, auto_id: int):
    try:
        auto = Auto.objects.get(id=auto_id)
        auto.is_sell = True
        Sales.objects.create(
            worker_id=pk, auto_id=auto_id, date=datetime.now(),
            really_cost=auto.selling_price
        )
        auto.save()
    except Exception:
        return render(
            request,
            "worker/error_sell_auto.html",
            {"pk": pk, "error": "Произошла ошибка! Пожалуйста, попробуйте позже."}
        )
    url = reverse_lazy('worker:auto', kwargs={'pk': pk})
    return redirect(url)



