from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('knihy/', views.KnihaListView.as_view(), name='knihy'),
    #re_path(r'^films/genres/(?P<genre_name>[\w-]+)/:?(?P<order>[\w-]*)$', views.FilmListView.as_view(), name='film_genre'),
    path('knihy/zanry/<str:genre_name>/', views.KnihaListView.as_view(), name='kniha_zanr'),
    path('knihy/<int:pk>/', views.KnihaDetailView.as_view(), name='kniha_detail'),
]