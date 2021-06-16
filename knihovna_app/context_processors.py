from knihovna_app.models import Genre

def genres(request):
    return {'genres': Genre.objects.all()}