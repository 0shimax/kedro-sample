from kedro.pipeline import Pipeline, node

from .nodes import split_data, train_model, evaluate_model


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="spliet_data_node",
                tags=["ds"],
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
                tags=["ds", "fit"],
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
                tags=["ds", "eval"],
            ),
        ]
    )
