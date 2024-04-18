from django.forms import ModelForm

from .models import Card


class CardModelForm(ModelForm):
    class Meta:
        model = Card
        fields = ["number", "suit"]
