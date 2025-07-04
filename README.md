
# 🎙️ Voice-Enabled Task Planner AI Agent

This project is a powerful, speech-based AI agent that allows users to create, query, and manage their tasks using natural spoken language. Built from the ground up, this agent demonstrates a complete, hands-free workflow from voice input to voice output, orchestrated through a modern AI stack.

---

## 🎯 Core Features

- **Hands-Free Interaction**: Manage your entire schedule without touching your keyboard.
- **Natural Language Understanding**: Uses OpenAI's GPT models to parse complex, unstructured commands (e.g., *“Remind me to call mom next Tuesday at 7pm”*).
- **Intelligent Intent Parsing**: Accurately identifies user intentions like adding, retrieving, or completing tasks.
- **Fuzzy Task Matching**: Marks tasks as complete even if the exact phrase isn’t matched (e.g., *“I finished the report”* → *“Submit Q3 financial report”*).
- **Persistent Storage**: Tasks are stored in a lightweight SQLite database for reliable persistence.
- **Real-Time Voice Feedback**: Confirms actions and reads your schedule aloud using Text-to-Speech.

---

## ⚙️ Tech Stack & Architecture

This project uses a modular AI pipeline:

```
Speech-to-Text ➔ LLM Intent Parser ➔ Task Manager ➔ Text-to-Speech
```

| Component             | Technology/Library            | Purpose                                         |
|-----------------------|-------------------------------|-------------------------------------------------|
| Speech-to-Text        | `SpeechRecognition`, `PyAudio` | Capturing and transcribing voice input          |
| Natural Language Core | `openai` (GPT-3.5 / GPT-4)     | Parsing user intent and extracting entities     |
| Database              | `sqlite3`                      | Storing and managing tasks                      |
| Text-to-Speech        | `pyttsx3`                      | Converting AI responses to audible speech       |
| Date/Time Parsing     | `dateparser`                   | Handling natural date expressions like "tomorrow" |
| Env Management        | `python-dotenv`                | Loading secure OpenAI API key                   |

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.8+
- An OpenAI API Key
- Homebrew (for macOS) for installing system dependencies

### 🧪 Installation

1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd voice_task_planner
```

2. **Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

> On Windows, use:
>
> ```bash
> venv\Scripts\activate
> ```

3. **Install System Dependencies**

- On **macOS**:

```bash
brew install portaudio
```

- On **Debian/Ubuntu**:

```bash
sudo apt-get update && sudo apt-get install portaudio19-dev python3-pyaudio
```

4. **Install Required Python Packages**

```bash
pip install -r requirements.txt
```

5. **Configure OpenAI API Key**

Create a `.env` file in the root directory and add your API key:

```env
OPENAI_API_KEY="sk-YourSecretKeyGoesHere"
```

---

## ▶️ Running the Agent

Start the application:

```bash
python main.py
```

Once launched, the agent will greet you and begin listening through your microphone for task-related commands.

---

## 🔥 Example Interactions

### ➕ Adding a Task

**You:**  
`"Remind me to submit the quarterly report at 4 PM on Friday"`  
**AI:**  
`"Got it! I've added the task: submit the quarterly report. It's scheduled for Friday, October 27 at 04:00 PM."`

---

### 📅 Querying Tasks

**You:**  
`"What's on my schedule for tomorrow?"`  
**AI:**  
`"You have 2 tasks scheduled for tomorrow: 1) Team sync at 10:00 AM. 2) Pay electricity bill."`

---

### ✅ Completing a Task

**You:**  
`"I've finished the team sync"`  
**AI:**  
`"Great! I've marked a task related to 'team sync' as complete."`

---

### 📋 Listing All Tasks

**You:**  
`"Show me all my pending tasks"`  
**AI:**  
`"You have a total of 3 pending tasks: 1) Pay electricity bill. 2) Submit the quarterly report for Friday, October 27..."`

---

### ❌ Exiting the Agent

**You:**
`"Goodbye"`
**AI:**
`"Goodbye!"`

---

## 📄 License

This project is released under the [MIT License](LICENSE).

---

## ✨ Contributions

Contributions, issues, and feature requests are welcome.
Feel free to open a pull request or issue.

---

## 💬 Acknowledgments

- [OpenAI](https://openai.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
