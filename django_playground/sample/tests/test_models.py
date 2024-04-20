import hypothesis
import hypothesis.extra.django
import hypothesis.strategies as st
import pytest
from django.core.validators import ValidationError

from ..models import Card, Number, Suit


class TestCardModel(hypothesis.extra.django.TestCase):
    @hypothesis.given(
        number=st.integers(min_value=Number.ACE.value, max_value=Number.KING.value),
        suit=st.sampled_from(Suit.values),
    )
    def test_card_creation(self, number: Number, suit: Suit):
        card = Card(number=number, suit=suit)
        card.full_clean()
        card.save()

        assert card.number == number
        assert card.suit == suit
        assert str(card) == f"{suit}{number}"

    @hypothesis.given(
        number=st.integers(min_value=14) | st.integers(max_value=0) | st.just(None),
        suit=st.sampled_from(Suit.values),
    )
    def test_invalid_number(self, number: int, suit: Suit):
        card = Card(number=number, suit=suit)
        with pytest.raises(ValidationError):
            card.full_clean()

    @hypothesis.given(
        number=st.integers(min_value=Number.ACE.value, max_value=Number.KING.value),
        suit=st.characters(exclude_characters=Suit.values) | st.just(None),
    )
    def test_invalid_suit(self, number: Number, suit: str):
        card = Card(number=number, suit=suit)
        with pytest.raises(ValidationError):
            card.full_clean()
