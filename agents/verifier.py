class Verifier:
    @staticmethod
    def verify_result(user_query, raw_data):
        answer = {}

        # If weather data exists
        if "weather" in raw_data:
            weather = raw_data["weather"]
            answer["weather"] = {
                "city": weather.get("city"),
                "temperature": str(weather.get("temperature_c")),
                "condition": weather.get("condition")
            }

        # If github data exists
        if "github" in raw_data:
            github_projects = []
            for repo in raw_data["github"]:
                github_projects.append({
                    "name": repo.get("name"),
                    "stars": str(repo.get("stars")),
                    "url": repo.get("url"),
                    "description": repo.get("description")
                })

            answer["github_projects"] = github_projects

        # If nothing worked
        if not answer:
            return {
                "status": "error",
                "answer": "No valid data returned from tools"
            }

        return {
            "status": "success",
            "answer": answer
        }
