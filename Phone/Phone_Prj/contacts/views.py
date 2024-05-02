from django.shortcuts import get_object_or_404, redirect, render
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
    
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        contact = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email
        )

        return redirect('list')
    return render(request, 'contacts/create.html')

def detail(request, id):
    contact = get_object_or_404(Phone, id = id)
    return render(request, 'contacts/detail.html', {'contact' :contact})

def update(request, id):
    contact = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.phone_num = request.POST.get('phone_num')
        contact.email = request.POST.get('email')
        contact.save()
        return redirect('list')
    return render(request, 'contacts/update.html', {'contact' :contact})
    

def delete(request, id):
    contact = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        contact.delete()
        return redirect('list')
    return render(request, 'contacts/delete.html', {'contact' :contact})
    








    







