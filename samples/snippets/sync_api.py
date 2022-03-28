# [START cloudoptimization_sync_api]

from google.cloud.optimization_v1.services.fleet_routing.client import FleetRoutingClient
from google.cloud.optimization_v1.types.fleet_routing import OptimizeToursRequest


def call_sync_api(request_file_name):
  """Call the sync api for fleet routing."""
  # Use the default credentials for the environment.
  fleet_routing_client = FleetRoutingClient()

  with open(request_file_name, 'r') as f:
    # The request must include the `parent` field with the value set to
    # 'projects/{YOUR_GCP_PROJECT_ID}'.
    fleet_routing_request = OptimizeToursRequest.from_json(f.read())
    # Send the request and print the response.
    # Fleet Routing will return a response by the earliest of the `timeout`
    # field in the request payload and the gRPC timeout specified below.
    fleet_routing_response = fleet_routing_client.optimize_tours(
        fleet_routing_request, timeout=100)
    print(fleet_routing_response)
    # If you want to format the response to JSON, you can do the following:
    # from google.protobuf.json_format import MessageToJson
    # json_obj = MessageToJson(fleet_routing_response._pb)

# [END cloudoptimization_sync_api]
