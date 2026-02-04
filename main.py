import sys
import logging
from agents.planner import Planner
from agents.executor import Executor
from agents.verifier import Verifier

logging.basicConfig(level=logging.INFO)

def main():
    print("\n--- 🤖 GenAI Ops Assistant ---")

    if len(sys.argv) > 1:
        user_query = sys.argv[1]
        print(f"User Query (CLI): {user_query}")
    else:
        user_query = input("How can I help you today? ")

    print("\n[1/3] Planning...")
    plan = Planner.generate_plan(user_query)
    logging.info(f"Plan: {plan}")

    print("\n[2/3] Executing Tools...")
    raw_data = Executor.run_tasks(plan["steps"])
    logging.info(f"Raw Results: {raw_data}")

    print("\n[3/3] Verifying...")
    final_answer = Verifier.verify_result(user_query, raw_data)

    print("\n✅ Final Answer:")
    print(final_answer)

if __name__ == "__main__":
    main()
