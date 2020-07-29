from django.forms import ModelForm
from tauschboerse.models import Gegenstand

class GegenstandForm(ModelForm):
    class Meta:
        model = Gegenstand
        fields = ["title", "description", "image", "status", "is_draft"]