# Copyright 2025 Google LLC
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
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


def get_state_match(query: str) -> str:
    """
    TODO: Finds a match within the nation for the donor.
    """
    
    return "Could not find a nationwide match."


PROMPT = 
"""
You are a nationwide area organ matcher. Go through nation's databases and find a match for the donor/donee.
If you don't have the nation, ask clarifying questions. Ask if the user has a nation in mind.

"""

root_agent = Agent(
    name="state_match_agent",
    model="gemini-2.5-flash", # Flexible model choice i.e. chatgpt, claude, deepseek etc.
    instruction=PROMPT,
    tools=[get_state_match],
)
