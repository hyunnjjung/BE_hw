from django.views.generic import ListView
from .models import Phone


class List(ListView):
    queryset = Phone.objects.all().order_by('name')
    template_name = 'contacts/list.html'
    context_object_name = 'contacts'

class Result(ListView):
    template_name = 'contacts/result.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        self.data = self.request.GET.get('data', '')  
        return Phone.objects.filter(name__contains=self.data).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data
        return context








    







