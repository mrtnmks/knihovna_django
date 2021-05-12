from django.shortcuts import render
from knihovna_app.models import Kniha, Priloha


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

def topten(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'topten.html',
    )