from django.shortcuts import render
from gegenstaende.models import Gegenstand
# Create your views here.
def gegenstaende_index(request):
    gegenstaende = Gegenstand.objects.all()
    context = {
        "gegenstaende": gegenstaende
        }
    return render(request, "gegenstaende_index.html", context)

def gegenstand_detail(request, gegenstand_pk): #pk = primary key
    gegenstand = Gegenstand.objects.get(pk=gegenstand_pk)
    context = {
        "gegenstand": gegenstand
        }
    return render(request, "gegenstand_detail.html", context)
