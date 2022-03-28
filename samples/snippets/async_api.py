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
    except GoogleAPICallError:
      print(operation.operation.error)


# [END cloudoptimization_async_api]
