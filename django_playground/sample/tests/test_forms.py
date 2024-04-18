import hypothesis
import hypothesis.extra.django
import hypothesis.strategies as st

from ..forms import CardModelForm
from ..models import Number, Suit


class TestCardForm(hypothesis.extra.django.TestCase):
    @hypothesis.given(
        number=st.integers(min_value=Number.ACE.value, max_value=Number.KING.value),
        suit=st.sampled_from(Suit.values),
    )
    def test_valid_form(self, number: Number, suit: Suit):
        form_data = {"number": number, "suit": suit}
        form = CardModelForm(data=form_data)

        assert form.is_valid()

        card = form.save()
        assert card.number == number
        assert card.suit == suit

    def test_blank_data(self):
        form = CardModelForm(data={})

        assert not form.is_valid()
        assert len(form.errors) == 2

    @hypothesis.given(
        number=st.integers(min_value=14) | st.integers(max_value=0) | st.just(None),
        suit=st.sampled_from(Suit.values),
    )
    def test_invalid_number(self, number: int, suit: Suit):
        form_data = {"number": number, "suit": suit}
        form = CardModelForm(data=form_data)

        assert not form.is_valid()
        assert len(form.errors) == 1

    @hypothesis.given(
        number=st.integers(min_value=1, max_value=13),
        suit=st.characters(exclude_characters=Suit.values) | st.just(None),
    )
    def test_invalid_suit(self, number: Number, suit: str):
        form_data = {"number": number, "suit": suit}
        form = CardModelForm(data=form_data)

        assert not form.is_valid()
        assert len(form.errors) == 1
