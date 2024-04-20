import typing

from django.db import models


class Number(models.IntegerChoices):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(models.TextChoices):
    DIAMOND = "♢", "ダイヤ"
    SPADE = "♠", "スペード"
    HEART = "♡", "ハート"
    CLUB = "♣", "クラブ"


class Card(models.Model):
    number = models.PositiveSmallIntegerField(choices=Number)
    suit = models.CharField(max_length=1, choices=Suit)

    class Meta:
        constraints: typing.ClassVar[list[models.CheckConstraint]] = [
            models.CheckConstraint(check=models.Q(number__in=Number.values), name="number_check"),
            models.CheckConstraint(check=models.Q(suit__in=Suit.values), name="suit_check"),
        ]

    def __str__(self) -> str:
        return f"{self.suit}{self.number}"
