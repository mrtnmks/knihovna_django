from knihovna_app.models import Zanr

def zanry(request):
    return {'zanry': Zanr.objects.all()}