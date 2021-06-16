from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    #re_path(r'^films/genres/(?P<genre_name>[\w-]+)/:?(?P<order>[\w-]*)$', views.FilmListView.as_view(), name='film_genre'),
    path('books/genres/<str:genre_name>/', views.BookListView.as_view(), name='book-genre'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    #path('films/<int:pk>/edit/', views.edit_film, name='film-edit'),
]