import factory
import factory.fuzzy

from ..models import Card, Number, Suit


class CardFactory(factory.django.DjangoModelFactory):
    number = factory.fuzzy.FuzzyChoice(choices=Number)
    suit = factory.fuzzy.FuzzyChoice(choices=Suit)

    class Meta:
        model = Card
