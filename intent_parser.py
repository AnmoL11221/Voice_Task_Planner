import openai
import os
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta
import dateparser

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_system_prompt():
    """Generates the system prompt with the current date."""
    current_date = datetime.now().strftime('%Y-%m-%d %A')
    tomorrow_date = (datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    return f"""
    You are an intelligent task planner assistant. Your job is to parse the user's natural language command
    and extract the intent and any relevant entities.
    The current date is {current_date}.

    You must classify the user's request into one of the following intents:
    - ADD_TASK: When the user wants to add a new task or reminder.
    - GET_TASKS: When the user wants to know what tasks they have scheduled for a specific day.
    - COMPLETE_TASK: When the user mentions finishing, completing, or being done with a task.
    - GET_ALL_TASKS: When the user asks for a general list of all their tasks, not specific to one day.
    - UNKNOWN: If the intent is unclear or not related to task management.

    For each intent, extract the following entities:
    - ADD_TASK:
      - "task_description" (string): The specific action to be done.
      - "due_date" (string, ISO 8601 format YYYY-MM-DD HH:MM:SS): The date and time for the task.
    - GET_TASKS:
      - "query_date" (string, ISO 8601 format YYYY-MM-DD): The date the user is asking about. Defaults to today if not specified.
    - COMPLETE_TASK:
      - "task_description" (string): The description of the task to be marked as complete. Extract the core task.
    - GET_ALL_TASKS:
        - No entities needed.

    Respond ONLY with a JSON object.

    --- EXAMPLES ---
    User: "remind me to submit the report at 4 PM today"
    AI: {{ "intent": "ADD_TASK", "entities": {{ "task_description": "submit the report", "due_date": "{datetime.now().strftime('%Y-%m-%d')} 16:00:00" }} }}

    User: "what's on my schedule for tomorrow"
    AI: {{ "intent": "GET_TASKS", "entities": {{ "query_date": "{tomorrow_date}" }} }}

    User: "what do i have to do today"
    AI: {{ "intent": "GET_TASKS", "entities": {{ "query_date": "{datetime.now().strftime('%Y-%m-%d')}" }} }}

    User: "I'm done with submitting the report"
    AI: {{ "intent": "COMPLETE_TASK", "entities": {{ "task_description": "submit the report" }} }}

    User: "okay I've finished the laundry"
    AI: {{ "intent": "COMPLETE_TASK", "entities": {{ "task_description": "laundry" }} }}

    User: "list all my tasks"
    AI: {{ "intent": "GET_ALL_TASKS", "entities": {{}} }}

    User: "what's the weather like"
    AI: {{ "intent": "UNKNOWN", "entities": {{}} }}
    """

def parse_intent_with_llm(user_input: str) -> dict:
    """Uses GPT to parse user input into a structured command."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": user_input}
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )

        parsed_response = json.loads(response.choices[0].message.content)
        print(f"🧠 LLM Parsed Intent: {parsed_response}")
        return parsed_response

    except Exception as e:
        print(f"❌ Error parsing intent with LLM: {e}")
        return {"intent": "UNKNOWN", "entities": {}}

def parse_and_format_date(date_str: str) -> datetime:
    """Uses dateparser to handle flexible date strings."""
    if not date_str:
        return None
    settings = {'PREFER_DATES_FROM': 'future', 'RETURN_AS_TIMEZONE_AWARE': False}
    return dateparser.parse(date_str, settings=settings)