import requests
import os

api_key = os.getenv("MIMO_OPENAI_API_KEY")
url = "https://ai.mimo.org/v1/openai/message"
headers = {"api-key": api_key}

def send_message(user_message, thread_id):
    body = {"message": user_message}
    if thread_id:
        body["threadId"] = thread_id
    response = requests.post(url, headers=headers, json=body)
    return response.json()

current_thread_id = None

while True:
    user_message = input("You: ")
    response_data = send_message(user_message, current_thread_id)
    latest_message = response_data.get("response")
    current_thread_id = response_data.get("threadId")
    print(f"GPT: {latest_message}")