<p align="center">
    <img src="./media/LifeBridgeLogo.png" alt="LifeBridge AI Logo" />
</p>

# LifeBridge AI - Intelligent Organ & Blood Matching System

Agentic AI for life-saving logistics: Instantly matches donors, alerts hospitals, and coordinates transport to cut delays and prevent organ or rare blood waste.

## Project Structure

This project is organized as follows:

```
agent-007-project/
├── app/                 # Core application code
│   ├── agent.py         # Main agent logic (root agent)
│   ├── server.py        # FastAPI backend server
│   ├── sub_agents/      # Local sub-agents used by the root agent
│   │   ├── local_match_agent.py            
│   │   ├── state_match_agent.py
│   │   ├── international_match_agent.py
│   │   ├── transport_agent.py
│   └── utils/           # Utility functions and helpers
├── .cloudbuild/         # CI/CD pipeline configurations for Google Cloud Build
├── deployment/          # Infrastructure and deployment scripts
├── notebooks/           # Jupyter notebooks for prototyping and evaluation
├── tests/               # Unit, integration, and load tests
├── Makefile             # Makefile for common commands
├── GEMINI.md            # AI-assisted development guide
└── pyproject.toml       # Project dependencies and configuration
```

## Requirements

Before you begin, ensure you have:
- **uv**: Python package manager (used for all dependency management in this project) - [Install](https://docs.astral.sh/uv/getting-started/installation/) ([add packages](https://docs.astral.sh/uv/concepts/dependencies/) with `uv add <package>`)
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)
- **Terraform**: For infrastructure deployment - [Install](https://developer.hashicorp.com/terraform/downloads)
- **make**: Build automation tool - [Install](https://www.gnu.org/software/make/) (pre-installed on most Unix-based systems)


## Quick Start (Local Testing)

Install required packages and launch the local development environment:



```bash
cd agent-007-project && make install && make playground
```

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `make install`       | Install all required dependencies using uv                                                  |
| `make playground`    | Launch local development environment with backend and frontend - leveraging `adk web` command.|
| `make backend`       | Deploy agent to Cloud Run (use `IAP=true` to enable Identity-Aware Proxy) |
| `make local-backend` | Launch local development server |
| `make test`          | Run unit and integration tests                                                              |
| `make lint`          | Run code quality checks (codespell, ruff, mypy)                                             |
| `make setup-dev-env` | Set up development environment resources using Terraform                         |
| `uv run jupyter lab` | Launch Jupyter notebook                                                                     |

For full command options and usage, refer to the [Makefile](Makefile).


## Usage



