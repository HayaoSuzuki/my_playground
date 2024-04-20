import typing

from django.forms import ModelForm

from .models import Card


class CardModelForm(ModelForm):
    class Meta:
        model: typing.ClassVar[typing.Type[Card]] = Card
        fields: typing.ClassVar[list[str]] = ["number", "suit"]
