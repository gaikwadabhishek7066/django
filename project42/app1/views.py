from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Book
# Create your views here.

def home(request):
    response = render(request, 'app1/home.html')
    return response 

def add_view(request):
    book_name = request.GET['title']
    author = request.GET['author']
    publication_year = request.GET['publication_year']
    genre = request.GET['genre']
    book = Book(title=book_name, author=author, publication_year=publication_year, genre=genre)
    book.save()
    response = render(request, 'app1/add.html',context={'msg': "Book added successfully"})
    return response
def add(request):
    response = render(request, 'app1/add.html')
    return response

def list_view(request):
    books = Book.objects.all()
    response = render(request, 'app1/booklist.html', context={'books': books})
    return response

def update_view(request):
    title = request.GET['title']
    book = Book.objects.get(title=title)
    book.author = request.GET['author']
    book.publication_year = request.GET['publication_year']
    book.genre = request.GET['genre']
    book.save()
    response = render(request, 'app1/update.html', context={'msg': 'Book updated successfully'})
    return response

def update(request):
    response = render(request, 'app1/update.html')
    return response

def delete_view(request):
    title = request.GET['title']
    book = Book.objects.get(title=title)
    book.delete()
    response = render(request, 'app1/delete.html', context={'msg': 'Book deleted successfully'})
    return response

def delete(request):
    response = render(request, 'app1/delete.html')
    return response