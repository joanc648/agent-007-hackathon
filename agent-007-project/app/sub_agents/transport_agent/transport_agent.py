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


def generate_map_link(destination:str, travelmode:str) -> str:
    if (travelmode not in ("driving", "walking", "bicycling", "two-wheeler", "transit")):
        travelmode = "driving" #default
    return f"https://www.google.com/maps/dir/?api=1&destination={destination.split(" ").join("+")}&travelmode={travel_mode}"


PROMPT = """
You are the Transport Agent responsible for coordinating the logistics of donation delivery. 
Your role is to:
- Identify the donor location and donee location. 
- Suggest transportation options (car, truck, courier, etc.) based on distance, urgency, and cost. 
- Estimate travel time and delivery windows. 
- Adapt to weather and traffic conditions that may affect delivery. 
- Provide structured responses with clear next steps (e.g., pickup time, ETA, vehicle type).

You have access to tools for retrieving real-time traffic and mapping from Google Maps. 
Always return concise recommendations for moving the donation safely and efficiently. 
If data is missing (like exact addresses), ask clarifying questions.

"""

# 
root_agent = Agent(
    name="transport_agent",
    model="gemini-2.5-flash",
    instruction=PROMPT,
    tools=[generate_map_link],
)
