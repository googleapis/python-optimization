from samples.snippets import sync_api

request_file_name = "resources/sync_request.json"


def test_call_sync_api(capsys):
  sync_api.call_sync_api(request_file_name)
  out, _ = capsys.readouterr()

  expected_strings = ["routes", "visits", "transitions", "metrics"]
  for expected_string in expected_strings:
    assert expected_string in out
