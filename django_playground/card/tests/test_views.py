import http

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

        response = client.get(reverse("card:list"))

        assert response.status_code == http.HTTPStatus.OK
        assert len(response.context["card_list"]) == 1

    @hypothesis.given(size=st.integers(min_value=0, max_value=100))
    def test_card_list_by_batch(self, size: int):
        client = Client()
        CardFactory.create_batch(size=size)

        response = client.get(reverse("card:list"))

        assert response.status_code == http.HTTPStatus.OK
        assert len(response.context["card_list"]) == size


class TestCardCreateView(hypothesis.extra.django.TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get(reverse("card:create"))

        assert response.status_code == http.HTTPStatus.OK

    @hypothesis.given(
        number=st.integers(min_value=Number.ACE.value, max_value=Number.KING.value),
        suit=st.sampled_from(Suit.values),
    )
    def test_valid_post_request(self, number: Number, suit: Suit):
        client = Client()
        form_data = {"number": number, "suit": suit}
        response = client.post(reverse("card:create"), data=form_data)

        assert response.status_code == http.HTTPStatus.FOUND
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
        response = client.post(reverse("card:create"), data=form_data)

        assert response.status_code == http.HTTPStatus.OK
        assert Card.objects.count() == 0

    @hypothesis.given(
        number=st.integers(min_value=Number.ACE.value, max_value=Number.KING.value),
        suit=st.characters(exclude_characters=Suit.values, codec="utf-8") | st.just(""),
    )
    def test_invalid_post_by_suit(self, number: int, suit: str):
        client = Client()
        form_data = {"number": number, "suit": suit}
        response = client.post(reverse("card:create"), data=form_data)

        assert response.status_code == http.HTTPStatus.OK
        assert Card.objects.count() == 0
