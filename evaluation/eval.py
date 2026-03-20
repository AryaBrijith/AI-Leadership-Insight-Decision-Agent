import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import initialize_agent, ask_agent

def run_evaluation():
    #Load questions
    with open('evaluation/test_questions.json', 'r') as f:
        tests = json.load(f)

    #Prepare the agent
    initialize_agent()
    
    print("\n---  Starting Automated Evaluation ---")
    passed = 0

    for test in tests:
        print(f"\nTesting: {test['question']}")
        
        # Get real answer from the agent
        actual_response = ask_agent(test['question'], ticker="ADBE")
        
        # To Check if the key fact is in the response
        if test['expected_answer'].lower() in actual_response.lower():
            print("Status: PASSED")
            passed += 1
        else:
            print("    Status: FAILED")
            print(f"   Expected keyword: '{test['expected_answer']}'")
            print(f"   Agent said: {actual_response[:100]}...")

    print(f"\n--- Final Score: {passed}/{len(tests)} ---")

if __name__ == "__main__":
    run_evaluation()