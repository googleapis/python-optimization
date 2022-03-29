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
