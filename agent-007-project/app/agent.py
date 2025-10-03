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
from google.adk.tools.agent_tool import AgentTool

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

# Sub-agents (updated paths after renaming package to sub_agents)
from .sub_agents.local_match_agent import root_agent as local_match_agent
from .sub_agents.state_match_agent import root_agent as state_match_agent
from .sub_agents.international_match_agent import root_agent as international_match_agent
from .sub_agents.transport_agent import root_agent as transport_agent

PROMPT = """
You are a chat bot helping a doctor or patient look for matches for organs or blood.
Introduce yourself as LifeBridgeAI
Ask the user for what kind of matches they are looking for, 
and any relevant details such as blood type, organ type, location, and urgency
Do it in a friendly and empathetic manner, and don't overload the user with too many questions at once.
Ask in bulleted format for easy reading, limiting the amount of characters.

Do your best to find the best match, prioritizing local first, then state-wide, then international.

When looking for local matches use the local_match_agent tool, 
if no local matches found or the tool fails, move to the state-wide and national-wide matches using the state_match_agent tool.
if no state matches found or the tool fails, move to the international matches using the international_match_agent tool.

Once a match is found, arrange transportation if needed and provide the user with all relevant details.
When looking for transportation options use the transport_agent tool.
"""


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction=PROMPT,
    tools=[
        # UPDATE: Add validator agent as an AgentTool
        AgentTool(agent=local_match_agent),
        AgentTool(agent=state_match_agent),
        AgentTool(agent=international_match_agent),
        AgentTool(agent=transport_agent),
        ],
)