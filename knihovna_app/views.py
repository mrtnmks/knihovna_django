from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from knihovna_app.forms import BookModelForm
from knihovna_app.models import Book, Genre, Attachment


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
            context['view_title'] = 'Knihy'
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


class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'knihovna/book_form.html'
    fields = ['isbn', 'title', 'plot', 'release_date', 'pages', 'poster', 'rate', 'genres', 'author']
    initial = {'rate': '5'}
    login_url = '/accounts/login/'
    permission_required = 'books.add_book'


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'knihovna/book_bootstrap_form.html'
    form_class = BookModelForm
    login_url = '/accounts/login/'
    permission_required = 'books.update_book'
    #fields = '__all__' # Not recommended (potential security issue if more fields added)


class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'knihovna/book_confirm_delete.html'
    success_url = reverse_lazy('books')
    login_url = '/accounts/login/'
    permission_required = 'books.delete_book'

def error_404(request, exception=None):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def error_403(request, exception=None):
    return render(request, 'errors/403.html')


def error_400(request, exception=None):
    return render(request, 'errors/400.html')


@never_cache
def clear_cache(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    cache.clear()
    return HttpResponse('Cache has been cleared')