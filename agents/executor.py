from tools.weather_tool import get_weather
from tools.github_tool import search_github

class Executor:
    @staticmethod
    def run_tasks(steps):
        results = {}

        for step in steps:
            tool = step["tool"]
            query = step["input"]

            try:
                if tool == "weather":
                    results["weather"] = get_weather(query)

                elif tool == "github":
                    results["github"] = search_github(query)

            except Exception as e:
                results[tool] = {"error": str(e)}

        return results
