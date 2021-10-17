from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .models import Negocio, Categ
from .forms import ContactForm

from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import time
# Create your views here.

def category_view(request):
    objs = Categ.objects.get(slug=slug)
    
    context = {
        'objs': objs,
    }
    return render(request, 'category_detail.html', context)
class NegocioListView(ListView):
    model = Negocio
    template_name = 'negocio_list.html'
    
    

class NegocioDetailView(FormMixin, DetailView):
    model = Negocio
    form_class = ContactForm
    template_name = 'negocio_detail.html'
    slug_field = 'slug'
    context_object_name = 'negocio'

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print(context)
        return context

    def post(self, request, slug, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                subject = form.cleaned_data['subject']
                mail = form.cleaned_data['mail']
                description = form.cleaned_data['description']
                form.save()
                time.sleep(1)
                
                
                print('valid \n',"subject: ", subject,'valid \n')
                form = ContactForm()
                

        else:
            form = ContactForm()
        # if request.method == 'POST':
        #     self.object = self.get_object()
        #     form = self.get_form()
        #     if form.is_valid():
        #         return self.form_valid(form)
        #     else:
        #         return self.form_invalid(form)
        return HttpResponseRedirect(reverse('negocio_detail', args=[slug]))

    
    