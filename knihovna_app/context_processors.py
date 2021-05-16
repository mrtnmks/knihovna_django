from knihovna_app.models import Kniha

def zanry(request):
    return {'zanry': Kniha.objects.all()}