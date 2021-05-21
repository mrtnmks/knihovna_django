from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from knihovna_app.models import Kniha, Priloha, Autor


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_knihas = Kniha.objects.all().count()
    knihas = Kniha.objects.order_by('vydani')[:3]

    context = {
        'num_knihas': num_knihas,
        'knihas': knihas
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class KnihaListView(ListView):
    model = Kniha

    context_object_name = 'films_list'   # your own name for the list as a template variable
    template_name = 'knihy/list.html'  # Specify your own template name/location
    paginate_by = 3

    def get_queryset(self):
        if 'nazev_zanru' in self.kwargs:
            return Kniha.objects.filter(kniha__nazev=self.kwargs['nazev_zanru']).all() # Get 5 books containing the title war
        else:
            return Kniha.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_knihas'] = len(self.get_queryset())
        if 'nazev_zanru' in self.kwargs:
            context['view_title'] = f"Žánr: {self.kwargs['nazev_zanru']}"
            context['view_head'] = f"Žánr knihy: {self.kwargs['nazev_zanru']}"
        else:
            context['view_title'] = 'Knihy'
            context['view_head'] = 'Přehled knih'
        return context


class KnihaDetailView(DetailView):
    model = Kniha

    context_object_name = 'kniha_detail'   # your own name for the list as a template variable
    template_name = 'knihy/detail.html'  # Specify your own template name/location


class ZanrListView(ListView):
    model = Kniha
    template_name = 'bloky/list_zanru.html'
    context_object_name = 'zanrs'
    queryset = Kniha.objects.order_by('titul').all()


class TopTenListView(ListView):
    model = Kniha
    template_name = 'bloky/top_ten.html'
    context_object_name = 'knihas'
    queryset = Kniha.objects.order_by('-hodnoceni').all()[:10]


class NovaKnihaListView(ListView):
    model = Kniha
    template_name = 'bloky/nove_knihy.html'
    context_object_name = 'knihas'
    queryset = Kniha.objects.order_by('vydani').all()
    paginate_by = 2