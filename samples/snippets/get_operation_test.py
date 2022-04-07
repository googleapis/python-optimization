# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import string
from google.cloud import optimization_v1
import pytest

import get_operation


@pytest.fixture(scope="function")
def operation_id() -> str:
    client = optimization_v1.FleetRoutingClient()

    model_configs = optimization_v1.AsyncModelConfig()
    model_configs.input_config.gcs_source.uri = "uri_value"
    model_configs.output_config.gcs_destination.uri = "uri_value"

    request = optimization_v1.BatchOptimizeToursRequest(
        parent="parent_value",
        model_configs=model_configs,
    )

    # Make the request
    operation = client.batch_optimize_tours(request=request)

    yield operation.operation.name


def test_get_operation_status(capsys: pytest.LogCaptureFixture, operation_id: str) -> None:
    get_operation.get_operation(operation_id)
    out, _ = capsys.readouterr()
    assert "Operation details" in out
