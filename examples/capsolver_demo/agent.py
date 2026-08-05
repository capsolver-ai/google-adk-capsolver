"""Google ADK agent using functions backed by CapSolver Agent."""

import asyncio
import json
import os

from capsolver_agent import create_executor
from google.adk.agents import Agent


capsolver = create_executor()


def get_capsolver_balance() -> dict[str, object]:
    """Return the CapSolver balance for the currently authorized account."""
    return asyncio.run(capsolver.execute("get_balance", {}))


def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> dict[str, object]:
    """Solve a supported CAPTCHA for a lawful, user-authorized workflow.

    Args:
        captcha_type: One of reCaptchaV2, reCaptchaV3, or cloudflare.
        website_url: The exact page URL supplied by the user or application.
        website_key: The CAPTCHA site key discovered by the authorized workflow.
    """
    result = asyncio.run(
        capsolver.execute(
            "solve_captcha",
            {
                "captcha_type": captcha_type,
                "website_url": website_url,
                "website_key": website_key,
            },
        )
    )
    # Round-trip ensures only JSON-compatible values are returned to ADK.
    return json.loads(json.dumps(result))


root_agent = Agent(
    name="capsolver_demo",
    model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
    description="Demonstrates CapSolver Agent tools in Google ADK.",
    instruction=(
        "Use CapSolver only for lawful, user-authorized workflows. "
        "Never invent a target URL, CAPTCHA type, or site key."
    ),
    tools=[get_capsolver_balance, solve_captcha],
)
