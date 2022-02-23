# pylint: disable=unused-argument

import pytest
import pandas as pd

from kedro.io import LambdaDataSet
from kedro.pipeline import node
from hellow_kedro.pipelines.data_processing.nodes import preprocess_companies, preprocess_shuttles, create_model_input_table


companies = pd.DataFrame({
    "id": [35029, 30292, 19032],
    "company_rating": ["100%", "67%", "67%"],
    "company_location":["Niue", "Anguilla", "Russian Federation"],
    "total_fleet_count":[4.0, 6.0, 4.0],
    "iata_approved":["f","f","f"]
})

preprocessed_companies = pd.DataFrame({
    "id": [35029, 30292, 19032],
    "company_rating": [1.0, 0.67, 0.67],
    "company_location":["Niue", "Anguilla", "Russian Federation"],
    "total_fleet_count":[4.0, 6.0, 4.0],
    "iata_approved":[False,False,False]
})


shuttles = pd.DataFrame({
    "id": [63561, 36260, 57015], 
    "shuttle_location": ["Niue", "Anguilla", "Russian"],
    "shuttle_type": ["Type V5", "Type V5", "Type V5"],
    "engine_type": ["Quantum", "Quantum", "Quantum"],
    "engine_vendor": ["ThetaBase Services", "ThetaBase Services", "ThetaBase Services"],
    "engines": [1,1,1],
    "passenger_capacity":[2,2,2],
    "cancellation_policy": ["strict", "strict", "moderate"], 
    "crew": [1,1,0],
    "d_check_complete": ["f", "t", "f"],
    "moon_clearance_complete": ["f", "f", "f"],
    "price": ["$1325.0", "$1780.0", "$1715.0"],
    "company_id": [35029, 30292, 19032]
})

preprocessed_shuttles = pd.DataFrame({
    "id": [63561, 36260, 57015], 
    "shuttle_location": ["Niue", "Anguilla", "Russian"],
    "shuttle_type": ["Type V5", "Type V5", "Type V5"],
    "engine_type": ["Quantum", "Quantum", "Quantum"],
    "engine_vendor": ["ThetaBase Services", "ThetaBase Services", "ThetaBase Services"],
    "engines": [1,1,1],
    "passenger_capacity":[2,2,2],
    "cancellation_policy": ["strict", "strict", "moderate"], 
    "crew": [1,1,0],
    "d_check_complete": [False, True, False],
    "moon_clearance_complete": [False, False, False],
    "price": [1325.0, 1780.0, 1715.0],
    "company_id": [35029, 30292, 19032]
})


reviews = pd.DataFrame({
    "shuttle_id":[63561, 36260, 57015],
    "review_scores_rating": [97.0, 90.0,95.0],
    "review_scores_comfort": [10.0, 8.0, 9.0],
    "review_scores_amenities": [9.0, 9.0, 10.0],
    "review_scores_trip":[9.0, 9.0, 10.0],
    "review_scores_crew": [9.0, 9.0, 10.0],
    "review_scores_location":[9.0, 9.0, 10.0],
    "review_scores_price":[9.0, 9.0, 10.0],
    "number_of_reviews": [133, 3, 14],
    "reviews_per_month": [1.65, 0.09, 0.14]
})

master_table = pd.DataFrame({
    "id": [],
    "review_scores_rating": [],
    "review_scores_comfort": [],
    "review_scores_amenities": [],
    "review_scores_trip":[],
    "review_scores_crew": [],
    "review_scores_location":[],
    "review_scores_price":[],
    "number_of_reviews": [],
    "reviews_per_month": [],
    "shuttle_location": [],
    "shuttle_type": [],
    "engine_type": [],
    "engine_vendor": [],
    "engines": [],
    "passenger_capacity":[],
    "cancellation_policy": [], 
    "crew": [],
    "d_check_complete": [],
    "moon_clearance_complete": [],
    "price": [],
    "company_id": [],
    "company_rating": [],
    "company_location":[],
    "total_fleet_count":[],
    "iata_approved":[]
})


@pytest.fixture
def valid_nodes_with_inputs():
    return [
        (node(preprocess_companies, "companies", "preprocessed_companies"), dict(companies=companies)),
        (node(preprocess_shuttles, "shuttles", "preprocessed_shuttles"), dict(shuttles=shuttles)),
        (node(create_model_input_table, ["preprocessed_shuttles","preprocessed_companies","reviews"], "master_table"), dict(preprocessed_shuttles=preprocessed_shuttles, preprocessed_companies=preprocessed_companies, reviews=reviews))
    ]


def test_valid_nodes0(valid_nodes_with_inputs):
    node_, input_ = valid_nodes_with_inputs[0]
    output = node_.run(input_)
    assert preprocessed_companies.equals(output["preprocessed_companies"])


def test_valid_nodes1(valid_nodes_with_inputs):
    node_, input_ = valid_nodes_with_inputs[1]
    output = node_.run(input_)
    assert preprocessed_shuttles.equals(output["preprocessed_shuttles"])


def test_valid_nodes2(valid_nodes_with_inputs):
    node_, input_ = valid_nodes_with_inputs[2]
    output = node_.run(input_)
    assert master_table.equals(output["master_table"])
