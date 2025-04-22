from django.views.generic import ListView

from auto.models import Auto


class AutoListView(ListView):
    model = Auto
    template_name = 'auto/list.html'
    context_object_name = 'auto'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
