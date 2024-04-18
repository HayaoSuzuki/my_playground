import hypothesis
import hypothesis.extra.django
import hypothesis.strategies as st
from django.test import Client
from django.urls import reverse

from ..models import Card, Number, Suit
from .factory import CardFactory


class TestCardListView(hypothesis.extra.django.TestCase):
    @hypothesis.given(
        number=st.integers(min_value=Number.ACE.value, max_value=Number.KING.value),
        suit=st.sampled_from(Suit.values),
    )
    def test_card_list_view(self, number: int, suit: str):
        client = Client()
        CardFactory(number=number, suit=suit)

        response = client.get(reverse("sample:list"))

        assert response.status_code == 200
        assert len(response.context["card_list"]) == 1


class TestCardCreateView(hypothesis.extra.django.TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get(reverse("sample:create"))

        assert response.status_code == 200

    @hypothesis.given(
        number=st.integers(min_value=1, max_value=13),
        suit=st.sampled_from(Suit.values),
    )
    def test_valid_post_request(self, number: Number, suit: Suit):
        client = Client()
        form_data = {"number": number, "suit": suit}
        response = client.post(reverse("sample:create"), data=form_data)

        assert response.status_code == 302
        assert Card.objects.count() == 1

        card = Card.objects.first()
        assert card.number == number
        assert card.suit == suit
        assert str(card) == f"{suit}{number}"

    @hypothesis.given(
        number=st.integers(min_value=14) | st.integers(max_value=0),
        suit=st.sampled_from(Suit.values),
    )
    def test_invalid_post_by_number(self, number: int, suit: str):
        client = Client()
        form_data = {"number": number, "suit": suit}
        response = client.post(reverse("sample:create"), data=form_data)

        assert response.status_code == 200
        assert Card.objects.count() == 0

    @hypothesis.given(
        number=st.integers(min_value=1, max_value=13),
        suit=st.characters(exclude_characters=Suit.values) | st.just(""),
    )
    def test_invalid_post_by_suit(self, number: int, suit: str):
        client = Client()
        form_data = {"number": number, "suit": suit}
        response = client.post(reverse("sample:create"), data=form_data)

        assert response.status_code == 200
        assert Card.objects.count() == 0
