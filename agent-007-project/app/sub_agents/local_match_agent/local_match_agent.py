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

import datetime
import os
from zoneinfo import ZoneInfo
from pathlib import Path
import pandas as pd

import google.auth
from google.adk.agents import Agent


_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

PROMPT = """
You are a local area organ matcher
Ask the user for their general location, their blood type, and the organ they need
Do you best to follow the following format: state, blood type, organ and the urgency
If the user provides a zip code or area, please ask the user to be more specific in their area

Return the outpu 
"""

# helper function for getting zip code

def get_organs_donors_local(query: str) -> str:
    """
    args: string containing question about how many organs needed in area
    - needs country, state and organ needed
    - connects to csv file
    springfield, o-, kidney, urgent


    returns: simple output of number of people in each zipcode

    """
    
    # Parse query
    # How to get this into this format from what user is inputting?
    parts = [p.strip().lower() for p in query.split(',')]
    state, blood_type, organ, urgency = parts[0], parts[1], parts[2], parts[3]


    

    # read sample csv data (path is relative to the repository root)
    project_root = Path(__file__).resolve().parents[3]
    mock_va_data_path = project_root / "sample_data" / "va_donor_data_sample.csv"

    df = pd.read_csv(mock_va_data_path)
    filtered_df = df.copy

    # get organ type
    filtered_df = filtered_df[filtered_df['organ available'].str.lower().str.lower().str.strip() == organ]
    # get blood type type
    filtered_df = filtered_df[filtered_df['donor-blood-type'].str.lower().str.lower().str.strip() == blood_type]

    # get state
    filtered_df = filtered_df[filtered_df['country'].str.lower().str.lower().str.strip() == state]


    #return f"There are {total_va_records} donors in your state and the amount of donors per zip code are: "



# 
root_agent = Agent(
    name="local_match_agent",
    model="gemini-2.5-flash", # Flexible model choice i.e. chatgpt, claude, deepseek etc.
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=[get_organs_donors_local],
)
