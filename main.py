from task_manager import TaskManager
from intent_parser import parse_intent_with_llm, parse_and_format_date
from voice_io import speak, listen_for_command
import datetime


def process_add_task(entities):
    description = entities.get("task_description")
    due_date_str = entities.get("due_date")

    if not description:
        speak("I'm sorry, I didn't catch the task description. Please try again.")
        return

    due_date = parse_and_format_date(due_date_str) if due_date_str else None

    task_manager.add_task(description, due_date)

    response = f"Got it! I've added the task: {description}."
    if due_date:
        human_readable_date = due_date.strftime("%A, %B %d at %I:%M %p")
        response += f" It's scheduled for {human_readable_date}."

    speak(response)

def process_get_tasks(entities):
    query_date_str = entities.get("query_date", datetime.date.today().isoformat())
    query_date = parse_and_format_date(query_date_str).date()

    tasks = task_manager.get_tasks(query_date)

    if not tasks:
        date_ref = "today" if query_date == datetime.date.today() else f"for {query_date.strftime('%A, %B %d')}"
        speak(f"You have no tasks scheduled {date_ref}.")
        return

    date_context = "today" if query_date == datetime.date.today() else f"for {query_date.strftime('%A, %B %d')}"
    response = f"You have {len(tasks)} task{'s' if len(tasks) > 1 else ''} scheduled {date_context}. "

    for i, task in enumerate(tasks):
        desc, due_date_str, _ = task
        due_date_obj = datetime.datetime.fromisoformat(due_date_str) if due_date_str else None
        time_info = f"at {due_date_obj.strftime('%I:%M %p')}" if due_date_obj and due_date_obj.time() != datetime.time.min else ""
        response += f"{i+1}) {desc} {time_info}. "
    speak(response)

def process_complete_task(entities):
    description = entities.get("task_description")
    if not description:
        speak("I'm not sure which task you want to complete. Please be more specific.")
        return

    updated_count = task_manager.complete_task(description)

    if updated_count > 0:
        speak(f"Great! I've marked a task related to '{description}' as complete.")
    else:
        speak(f"I couldn't find a pending task that matches '{description}'.")

def process_get_all_tasks():
    tasks = task_manager.get_all_pending_tasks()
    if not tasks:
        speak("You have no pending tasks at the moment. Great job!")
        return

    response = f"You have a total of {len(tasks)} pending task{'s' if len(tasks) > 1 else ''}. "
    for i, task in enumerate(tasks):
        desc, due_date_str, _ = task
        if due_date_str:
            due_date_obj = datetime.datetime.fromisoformat(due_date_str)
            date_info = f" for {due_date_obj.strftime('%A, %B %d at %I:%M %p')}"
        else:
            date_info = ""
        response += f"{i+1}) {desc}{date_info}. "
    speak(response)


def main():
    """Main application loop."""
    speak("Hello! I am your voice-enabled task planner. How can I help you today?")
    while True:
        command = listen_for_command()

        if command:
            if any(word in command for word in ["exit", "quit", "goodbye", "stop"]):
                speak("Goodbye!")
                break

            parsed_command = parse_intent_with_llm(command)
            intent = parsed_command.get("intent")
            entities = parsed_command.get("entities", {})

            if intent == "ADD_TASK":
                process_add_task(entities)
            elif intent == "GET_TASKS":
                process_get_tasks(entities)
            elif intent == "COMPLETE_TASK":
                process_complete_task(entities)
            elif intent == "GET_ALL_TASKS":
                process_get_all_tasks()
            else:
                speak("I'm sorry, I'm not sure how to help with that. You can ask me to add a task, list tasks, or complete a task.")
        else:
            pass

if __name__ == "__main__":
    task_manager = TaskManager()
    try:
        main()
    finally:
        task_manager.close()
        print("Application terminated. Database connection closed.")