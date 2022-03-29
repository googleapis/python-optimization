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

# [START cloudoptimization_async_api]

import json
import sys

from google.api_core.exceptions import GoogleAPICallError
from google.cloud.optimization_v1.services.fleet_routing.client import FleetRoutingClient
from google.cloud.optimization_v1.types.fleet_routing import BatchOptimizeToursRequest


def call_async_api(request_file_name):
  """Call the async api for fleet routing."""
  # Use the default credentials for the environment to authenticate the client.
  fleet_routing_client = FleetRoutingClient()

  with open(request_file_name, 'r') as f:
    # The request must include the "parent" field with the value set to
    # "projects/{YOUR_GCP_PROJECT_ID}".
    fleet_routing_request = BatchOptimizeToursRequest.from_json(f.read())
    # The timeout argument for the gRPC call is independent from the `timeout`
    # field in the request's OptimizeToursRequest message(s).
    operation = fleet_routing_client.batch_optimize_tours(fleet_routing_request)
    details = fleet_routing_client._transport.operations_client.get_operation(
        operation.operation.name)
    print(details)

    try:
      # Block to wait for the job to finish.
      result = operation.result()
      print(result)
      # Do you stuff.
    except:
      print(operation.operation.error)


# [END cloudoptimization_async_api]
