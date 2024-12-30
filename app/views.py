from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Order



class HomepageView(TemplateView):
    template_name = 'app/home.html'

class AboutpageView(TemplateView):
        template_name = 'app/about.html'

class ContactpageView(TemplateView):
    template_name = 'app/contact.html'
    
class OrderListView(ListView):
    model = Order
    template_name = 'app/order_list.html'
    context_object_name = 'orders'
    
    
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'app/order_detail.html'
    context_object_name = 'order'
    
class OrderCreateView(CreateView):
    model = Order  
    fields = ['customer','stage']
    template_name = 'app/order_create.html'
    # success_url = reverse_lazy('order_list')
    
      

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'app/order_update.html'
    fields = ['customer','stage']


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'app/order_delete.html'
    success_url = reverse_lazy('order_list')
    

    
    




