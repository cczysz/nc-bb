#!/usr/bin/env python3

from typing import List
from tobacco_road.predictions import Predictions


class SmiffClass:
    """Collects all predictions for a given class."""

    def __init__(
        self,
        *args,
        game_date: str = None,
        predictions: List[Predictions] = None,
        **kwargs
    ):
        self.game_date = game_date
        self.predictions = predictions

    @classmethod
    def read_predictions(cls, game_date: str = None, predictions: str = None):
        prediction_list = list(Predictions.generate(predictions))
        return cls(game_date=game_date, predictions=prediction_list)
