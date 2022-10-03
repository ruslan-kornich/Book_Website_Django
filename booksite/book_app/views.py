from django.shortcuts import render
from .models import Book, Category


def home(request):
    recommended_books = Book.objects.filter(recommended_books=True)
    fiction_books = Book.objects.filter(fiction_books=True)
    business_books = Book.objects.filter(business_books=True)
    return render(request, 'home.html', {'recommended_books': recommended_books,
                                         'business_books': business_books,
                                         'fiction_books': fiction_books
                                         })


def all_books(request):
    book = Book.objects.all()
    return render(request, 'all_books.html', {'book': book})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'genre_detail.html', {'category': category})


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith=book_category)
    return render(request, 'book_detail.html', {'book': book, 'similar_books': similar_books})


def search_book(request):
    searched_books = Book.objects.filter(title__icontains=request.POST.get('name_of_book'))
    return render(request, 'search_book.html', {'searched_books': searched_books})
