from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from knihovna_app.forms import BookModelForm
from knihovna_app.forms import Book, Genre, Attachment


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    books = Book.objects.order_by('-rate')[:3]

    context = {
        'num_books': num_books,
        'books': books
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(ListView):
    model = Book

    context_object_name = 'books_list'   # your own name for the list as a template variable
    template_name = 'book/list.html'  # Specify your own template name/location
    paginate_by = 3

    def get_queryset(self):
        if 'genre_name' in self.kwargs:
            return Book.objects.filter(genres__name=self.kwargs['genre_name']).all() # Get 5 books containing the title war
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_books'] = len(self.get_queryset())
        if 'genre_name' in self.kwargs:
            context['view_title'] = f"Žánr: {self.kwargs['genre_name']}"
            context['view_head'] = f"Žánr knihy: {self.kwargs['genre_name']}"
        else:
            context['view_title'] = 'Filmy'
            context['view_head'] = 'Přehled knih'
        return context


class BookDetailView(DetailView):
    model = Book

    context_object_name = 'book_detail'   # your own name for the list as a template variable
    template_name = 'book/detail.html'  # Specify your own template name/location


class GenreListView(ListView):
    model = Genre
    template_name = 'blocks/genre_list.html'
    context_object_name = 'genres'
    queryset = Genre.objects.order_by('name').all()


class TopTenListView(ListView):
    model = Book
    template_name = 'blocks/top_ten.html'
    context_object_name = 'books'
    queryset = Book.objects.order_by('-rate').all()[:10]


class NewBooksistView(ListView):
    model = Book
    template_name = 'blocks/new_books.html'
    context_object_name = 'books'
    queryset = Book.objects.order_by('release_date').all()
    paginate_by = 2


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'plot', 'release_date', 'pages', 'poster', 'rate', 'genres']
    initial = {'rate': '5'}


class BookUpdate(UpdateView):
    model = Book
    template_name = 'knihovna/film_bootstrap_form.html'
    form_class = BookModelForm
    #fields = '__all__' # Not recommended (potential security issue if more fields added)


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')