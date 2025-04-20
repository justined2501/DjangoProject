from django.views.generic import TemplateView


class NewsView(TemplateView):
    template_name = 'news/list.html'
    context_object_name = 'news'
