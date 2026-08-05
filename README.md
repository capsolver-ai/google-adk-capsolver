# Google ADK + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/google-adk-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/google-adk-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable Google Agent Development Kit examples using the official [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent) executor.

> This repository contains an ADK demo application only. It does not publish a separate `google-adk-capsolver` package.

## Repository scope

Google ADK automatically converts typed Python functions into agent tools. The example keeps those functions thin and delegates all CapSolver behavior to the shared agent library.

## Quick start

```bash
git clone https://github.com/capsolver-ai/google-adk-capsolver.git
cd google-adk-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Export the values in [`.env.example`](.env.example), then launch the demo:

```bash
adk web examples
```

You can also use `adk run examples/capsolver_demo` for a terminal session.

## Key integration code

```python
from capsolver_agent import create_executor
from google.adk.agents import Agent

capsolver = create_executor()

def get_capsolver_balance() -> dict[str, object]:
    return asyncio.run(capsolver.execute("get_balance", {}))

root_agent = Agent(name="capsolver_demo", model="gemini-2.5-flash", tools=[get_capsolver_balance])
```

See [`examples/capsolver_demo/agent.py`](examples/capsolver_demo/agent.py) for the full demo.

## Project layout

```text
examples/capsolver_demo/agent.py  Google ADK root agent and tools
requirements.txt                  Shared SDK repositories plus Google ADK
tests/test_demo.py                 Offline validation
.github/workflows/ci.yml           Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver for AI agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [Google ADK function tools](https://adk.dev/tools-custom/function-tools/)

## Responsible use

Use the example only for lawful, user-authorized, terms-compliant automation. Never commit secrets or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

Google ADK is a third-party project. This repository is maintained by CapSolver and is not affiliated with or endorsed by Google.
