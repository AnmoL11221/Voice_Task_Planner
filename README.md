# Voice-Enabled Task Planner AI Agent

This project is a powerful, speech-based AI agent that allows users to create, query, and manage their tasks using natural spoken language. Built from the ground up, this agent demonstrates a complete, hands-free workflow from voice input to voice output, orchestrated through a modern AI stack.
🎯 Core Features
Hands-Free Interaction: Manage your entire schedule without touching your keyboard.
Natural Language Understanding: Uses OpenAI's GPT models to parse complex, unstructured commands (e.g., "Remind me to call mom next Tuesday at 7pm").
Intelligent Intent Parsing: Accurately identifies user intentions like adding, retrieving, or completing tasks.
Fuzzy Task Matching: Mark tasks as complete even if you don't say the exact description (e.g., "I finished the report" can complete "Submit Q3 financial report").
Persistent Storage: Tasks are saved in a lightweight SQLite database, so your schedule is always preserved.
Real-time Voice Feedback: The agent confirms actions and reads your schedule aloud using Text-to-Speech.
⚙️ Tech Stack & Architecture
This project showcases a classic agent orchestration pipeline:
Speech-to-Text (STT) ➔ LLM Intent Parser ➔ Task Manager (DB) ➔ Text-to-Speech (TTS)
Speech-to-Text: SpeechRecognition library (with Google Speech-to-Text engine) captures and transcribes microphone input.
LLM Intent Parser: The transcribed text is sent to an OpenAI GPT model (gpt-3.5-turbo) with a carefully engineered system prompt. The LLM's role is to act as a "function-caller," returning a structured JSON object containing the user's intent and extracted entities (task description, dates, times).
Task Manager: This module acts as the "tool" the agent uses. It takes the structured data from the LLM and performs CRUD (Create, Read, Update, Delete) operations on a SQLite database.
Text-to-Speech: The result or confirmation message is converted back into spoken words using pyttsx3 for immediate audio feedback.
| Component             | Technology/Library        | Purpose                                      |
|-----------------------|--------------------------|----------------------------------------------|
| Speech-to-Text        | SpeechRecognition / PyAudio | Capturing and transcribing voice           |
| Natural Language Core | openai (GPT-3.5/4)       | Parsing intent and entities                  |
| Database              | sqlite3                  | Storing and retrieving tasks                 |
| Text-to-Speech        | pyttsx3                  | Converting text responses to speech          |
| Date/Time Parsing     | dateparser               | Handling flexible date formats ("tomorrow")  |
| Environment Mgmt      | python-dotenv            | Managing API keys securely                   |

🚀 Getting Started
Follow these steps to get the agent running on your local machine.
Prerequisites
Python 3.8+
An OpenAI API Key
Homebrew (for macOS users) to install system dependencies.
Installation
Clone the repository:
Generated bash
git clone <your-repo-url>
cd voice_task_planner
Use code with caution.
Bash
Create and activate a virtual environment:
Generated bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
On Windows, use venv\Scripts\activate
Install system dependencies:
On macOS (using Homebrew):
Generated bash
brew install portaudio
Use code with caution.
Bash
On Debian/Ubuntu Linux:
Generated bash
sudo apt-get update && sudo apt-get install portaudio19-dev python3-pyaudio
Use code with caution.
Bash
Install the required Python packages:
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
Set up your API Key:
Create a file named .env in the root of the project directory.
Add your OpenAI API key to this file:
Generated env
OPENAI_API_KEY="sk-YourSecretKeyGoesHere"
Use code with caution.
Env
Running the Agent
With your virtual environment active, simply run the main script:
Generated bash
python main.py
Use code with caution.
Bash
The agent will greet you, and the microphone will begin listening for your command.
🔥 Example Interactions
Adding a Task:
🗣️ You: "Remind me to submit the quarterly report at 4 PM on Friday"
🤖 AI: "Got it! I've added the task: submit the quarterly report. It's scheduled for Friday, October 27 at 04:00 PM."
Querying Tasks:
🗣️ You: "What's on my schedule for tomorrow?"
🤖 AI: "You have 2 tasks scheduled for tomorrow. 1) Team sync at 10:00 AM. 2) Pay electricity bill."
Completing a Task:
🗣️ You: "I've finished the team sync"
🤖 AI: "Great! I've marked a task related to 'team sync' as complete."
Listing All Tasks:
🗣️ You: "Show me all my pending tasks"
🤖 AI: "You have a total of 3 pending tasks. 1) Pay electricity bill. 2) Submit the quarterly report for Friday, October 27... "
Exiting the Agent:
🗣️ You: "Goodbye"
🤖 AI: "Goodbye!"