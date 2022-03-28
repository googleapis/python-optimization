from samples.snippets import async_api

# TODO(developer): Replace the variables in the file before use.
# A sample request model can be found at resources/async_request_model.json.
request_file_name = "resources/async_api_request.json"


def test_call_async_api(capsys):
  async_api.call_async_api(request_file_name)
  out, _ = capsys.readouterr()

  expected_strings = ["name", "metadata", "type_url", "response"]
  for expected_string in expected_strings:
    assert expected_string in out
