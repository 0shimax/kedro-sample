# pylint: disable=unused-argument

import pytest
import pandas as pd

import kedro
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline, node
from kedro.pipeline.pipeline import (
    CircularDependencyError,
    ConfirmNotUniqueError,
    OutputNotUniqueError,
    _strip_transcoding,
    _transcode_split,
)
from kedro.runner import SequentialRunner
from hellow_kedro.pipelines.data_processing.pipeline import create_pipeline
from hellow_kedro.pipelines.data_processing.nodes import preprocess_companies, preprocess_shuttles, create_model_input_table


@pytest.fixture
def str_node_inputs_list():
    return {
        "nodes": [
            (node(preprocess_companies, "companies", "preprocessed_companies", name="preprocess_companies_node")),
            (node(preprocess_shuttles, "shuttles", "preprocessed_shuttles", name="preprocess_shuttles_node")),
            (node(create_model_input_table, ["preprocessed_shuttles","preprocessed_companies","reviews"], "master_table", name="create_master_table_node"))
        ],
        "free_inputs": ["companies", "shuttles", "reviews"],
        "outputs": ["master_table"],
    }


def test_pipeline_nodes(str_node_inputs_list):
    nodes = str_node_inputs_list["nodes"]
    pipeline = create_pipeline()

    for node_true, node_created in zip(nodes, pipeline.nodes) :
        assert node_created.func == node_true.func
        assert node_created.inputs == node_true.inputs
