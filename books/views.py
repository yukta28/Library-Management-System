from django.urls import path
from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.forms import ModelForm
from .forms import BookForm



# Create your views here.

class BookForm(ModelForm):
    class Meta:
        model = Book
        Bookfields = ['title', 'author', 'publication_dat', 'isbn']
        
def index(request):
    return render(request, book_list.html)
        
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
        
def book_create(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                return redirect('book_list')
            except ValidationError as e:
                form.add_error(None, e)
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = Book.object.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance = book)
    return render(request, 'books/book_form.html',{'form': form, 'object': book})

def book_delete(request, pk):
    book = Book.object.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html',{'object': book})

    





   
            
            
    
    
