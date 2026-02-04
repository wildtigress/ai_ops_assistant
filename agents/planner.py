import json
from llm.client import call_llm

class Planner:
    @staticmethod
    def generate_plan(user_query: str):
        prompt = f"""
You are a Planner Agent.

Convert the user request into a JSON plan.

Rules:
- Output ONLY valid JSON
- No explanations
- Follow this schema exactly:

{{
  "steps": [
    {{
      "tool": "weather" | "github",
      "input": "string"
    }}
  ]
}}

User request: "{user_query}"

Examples:

User: "What is the weather in Paris?"
Output:
{{"steps":[{{"tool":"weather","input":"Paris"}}]}}

User: "Find GitHub repositories about chatbots"
Output:
{{"steps":[{{"tool":"github","input":"chatbots"}}]}}

User: "What is the weather in Paris and find GitHub projects about weather APIs"
Output:
{{"steps":[
  {{"tool":"weather","input":"Paris"}},
  {{"tool":"github","input":"weather APIs"}}
]}}
"""

        response = call_llm(prompt)

        try:
            plan = json.loads(response)
            if "steps" not in plan:
                raise ValueError("Invalid plan format")
            return plan
        except Exception:
            return {"steps": []}
