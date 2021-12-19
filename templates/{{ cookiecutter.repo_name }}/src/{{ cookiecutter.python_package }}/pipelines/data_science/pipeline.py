from kedro.pipeline import Pipeline, node

from .nodes import # evaluate_model, split_data, train_model


def create_pipeline(**kwargs):
    return Pipeline([node()])
