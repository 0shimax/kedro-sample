from typing import List
from pydantic import BaseModel
import numpy as np


class FloatFeatures(BaseModel):
    engines: float
    passenger_capacity: float
    crew: float
    company_rating: float
    review_scores_rating: float

    def to_numpy(self):
        return np.array(
            [
                self.engines,
                self.passenger_capacity,
                self.crew,
                self.company_rating,
                self.review_scores_rating,
            ]
        ).astype(np.float32)


class CategoricalFeatures(BaseModel):
    d_check_complete: str
    moon_clearance_complete: str
    iata_approved: str

    def to_numpy(self):
        return np.array(
            [
                self.d_check_complete,
                self.moon_clearance_complete,
                self.iata_approved,
            ]
        ).astype(str)


class PredictionResult(BaseModel):
    predicted: List[float]

class Features(BaseModel):
    float_features: List[FloatFeatures]
    categorical_features: List[CategoricalFeatures]

    @classmethod
    def to_numpy(cls, x_fetures):
        return [v.to_numpy() for v in x_fetures]