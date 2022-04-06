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

import os

import google.auth
from google.cloud import optimization_v1
import pytest

import get_operation


@pytest.fixture(scope="function")
def operation_id():
    _, project_id = google.auth.default()

    client = optimization_v1.FleetRoutingClient()
    project_location = f"projects/{project_id}/locations/us-central1"

    generator = client._transport.operations_client.list_operations(
        project_location, filter_=""
    ).pages
    page = next(generator)
    operation = next(page)
    yield operation.name


def test_get_operation_status(capsys: pytest.LogCaptureFixture, operation_id):
    get_operation.get_operation(operation_id)
    out, _ = capsys.readouterr()
    assert "Operation details" in out
