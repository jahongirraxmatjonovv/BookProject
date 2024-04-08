from django.shortcuts import render
from django.views.generic import ListView , DetailView,CreateView,UpdateView,DeleteView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import *
from .bookform  import *

class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'
    ordering = 'title'
    
class BookDetail(DetailView):
    model = Book
    template_name = 'book-detail.html'
    context_object_name = 'book'
    ordering = 'title'
class BookCreate(CreateView):
    model = Book
    class_form = BookForm
    template_name = 'book-create.html'
    fields = ['title','author', 'price','publisher','image']
    success_url = reverse_lazy('book-list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book-update.html'
    success_url = reverse_lazy('book-list')

class BookDelete(DeleteView):
    model = Book
    template_name = 'book-delete.html'
    success_url = reverse_lazy('book-list')

    