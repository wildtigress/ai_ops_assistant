🤖 AI Operations Assistant (GenAI Multi-Agent System)
📌 Overview

This project implements a Multi-Agent AI Operations Assistant that accepts a natural language query, generates a structured plan using an LLM, executes real API calls, verifies the results, and returns a clean structured response.

It demonstrates:

Agent-based reasoning (Planner, Executor, Verifier)

LLM-powered planning and validation

Integration with real third-party APIs

End-to-end runnable CLI application

This project fulfills the requirements of the 24-Hour GenAI Intern Assignment – AI Operations Assistant.

🏗️ Architecture
User Query
   ↓
Planner Agent (LLM → JSON plan)
   ↓
Executor Agent (API calls)
   ↓
Verifier Agent (LLM validation)
   ↓
Final Structured Output

Agents:

Planner Agent: Converts user input into a structured JSON plan with required tools.

Executor Agent: Executes each step by calling the appropriate API tool.

Verifier Agent: Validates results, fixes formatting, and ensures correct structured output.

🔌 APIs & Tools Used

WeatherAPI – Fetches real-time weather data
https://www.weatherapi.com/api-explorer.aspx

GitHub Search API – Searches repositories by keyword

Groq LLM API (OpenAI compatible) – Used for:

Planning (Planner Agent)

Verification & formatting (Verifier Agent)

📁 Project Structure
ai_ops_assistant/
├── agents/
│   ├── __init__.py
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
├── tools/
│   ├── __init__.py
│   ├── weather_tool.py
│   └── github_tool.py
├── llm/
│   ├── __init__.py
│   └── client.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/wildtigress/ai_ops_assistant.git
cd ai_ops_assistant

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create .env file

Create a .env file in project root:

GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weatherapi_key

▶️ Usage (CLI)

Run the assistant from command line:

python main.py "Your query here"

🧪 Example Queries
python main.py "What is the weather in London?"

python main.py "Find GitHub repositories about weather APIs"

python main.py "What is the weather in Paris and find GitHub projects about weather APIs"

📤 Sample Output
{
  "status": "success",
  "answer": {
    "weather": {
      "city": "Paris",
      "temperature": "9.1",
      "condition": "Overcast"
    },
    "github_projects": [
      {
        "name": "open-meteo",
        "stars": "4659",
        "url": "https://github.com/open-meteo/open-meteo",
        "description": "Free Weather Forecast API"
      }
    ]
  }
}

🧠 Error Handling

API failures are handled gracefully

Partial results are returned if one tool fails

Verifier Agent ensures JSON output correctness

LLM retries invalid structured outputs

🚀 Features

Multi-agent architecture (Planner, Executor, Verifier)

Real-time API integration

LLM-powered planning & validation

CLI interface

Clean structured JSON output

Secure environment variable handling

🔮 Future Improvements

Caching API responses

Parallel tool execution

Cost tracking per request

Streamlit or FastAPI UI

Logging dashboard

Request history

📜 License

This project is licensed under the MIT License.
See the LICENSE file for details.

👩‍💻 Author

Samiksha Barnwal
GitHub: https://github.com/wildtigress
