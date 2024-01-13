from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'book_outlet/index.html',context={'books':books})

def book_detail(request,book_slug):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book,slug=book_slug)
    return render(request,'book_outlet/book_detail.html',context={
        'title':book.title,
        'author':book.author,
        'rating':book.rating,
        'is_bestseller':book.is_bestselling,})