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

def get_organs_donors_local(query: str) -> str:
    """
    args: string containing question about how many organs needed in area
    - needs country, state and organ needed
    - connects to csv file

    returns: simple output of number of people in each zipcode

    """
    # Gets state
    if "virginia" in query.lower() or "va" in query.lower():
        state_area = "Virginia"
    else:
        return f"Sorry, I don't have organ information for query: {query}."
    # read sample csv data (path is relative to the repository root)
    project_root = Path(__file__).resolve().parents[3]
    mock_va_data_path = project_root / "sample_data" / "va_donor_data_sample.csv"

    df = pd.read_csv(mock_va_data_path)
    # get num in state
    df['state'] = df['state'].str.strip().str.title()
    virginia_df = df[df['state'] == 'Virginia']
        
    total_va_records = len(virginia_df)    # filter zip codes

    # return number in each zip
    zip_counts = virginia_df['zip'].astype(str).str.strip()
        
    # Filter out records where ZIP is 'N/A' or NaN before counting
    zip_counts = zip_counts[zip_counts.str.upper() != 'N/A']
    zip_counts = zip_counts[zip_counts.str.len() > 1]
    
    zip_code_breakdown = zip_counts.value_counts().sort_values(ascending=False)

    return f"There are {total_va_records} donors in your state and the amount of donors per zip code are: {zip_code_breakdown}"



# 
root_agent = Agent(
    name="local_match_agent",
    model="gemini-2.5-flash", # Flexible model choice i.e. chatgpt, claude, deepseek etc.
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=[get_organs_donors_local],
)
