# Generated by Django 5.0.4 on 2024-04-18 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        choices=[
                            (1, "Ace"),
                            (2, "Two"),
                            (3, "Three"),
                            (4, "Four"),
                            (5, "Five"),
                            (6, "Six"),
                            (7, "Seven"),
                            (8, "Eight"),
                            (9, "Nine"),
                            (10, "Ten"),
                            (11, "Jack"),
                            (12, "Queen"),
                            (13, "King"),
                        ],
                        validators=[
                            django.core.validators.MaxValueValidator(13),
                            django.core.validators.MinValueValidator(1),
                        ],
                    ),
                ),
                (
                    "suit",
                    models.CharField(
                        choices=[
                            ("♢", "ダイヤ"),
                            ("♠", "スペード"),
                            ("♡", "ハート"),
                            ("♣", "クラブ"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="card",
            constraint=models.CheckConstraint(
                check=models.Q(("number__in", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])),
                name="number_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="card",
            constraint=models.CheckConstraint(
                check=models.Q(("suit__in", ["♢", "♠", "♡", "♣"])), name="suit_check"
            ),
        ),
    ]
