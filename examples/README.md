# Examples

`capsolver_demo/agent.py` exports the `root_agent` expected by Google ADK. ADK turns the two Python functions into tools; both delegate to `capsolver_agent.create_executor()`.

From the repository root, run `adk web examples` or `adk run examples/capsolver_demo` after installing `requirements.txt` and exporting `.env.example` values.
