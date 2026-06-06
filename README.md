# AI Chatbot Web Interface

A clean, web-based chatbot interface built with **Python** and **Gradio**, powered by the **Google Generative AI (Gemini 3 Flash Preview) API**. This application maintains a continuous session conversation history, allowing for context-aware, natural interactions directly in your browser.

## Features

* **Powered by Gemini 3 Flash Preview:** Uses the high-speed reasoning model designed for multi-turn chat and advanced agentic workflows.
* **Contextual Memory:** Maintains full conversation history during a session to provide relevant, continuous answers.
* **Sleek Gradio Interface:** A modern, responsive, and minimalist chat UI that runs locally or can be easily shared via a public link.
* **Simple Configuration:** Lightweight setup using environment variables for secure API key management.

---

## Getting Started

### Prerequisites

* Python 3.8 or higher
* A Google AI Studio API Key (Get one from [Google AI Studio](https://aistudio.google.com/))

### Installation

1. **Clone the repository:**
```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
Install the required dependencies:

Bash
   pip install -r requirements.txt
Setting Up the API Key
The application safely looks for your API key as an environment variable. Set it up using your terminal:

Linux/macOS:

Bash
    export GEMINI_API_KEY="your_actual_api_key_here"
    ```
* **Windows (Command Prompt):**
```cmd
    set GEMINI_API_KEY="your_actual_api_key_here"
    ```
* **Windows (PowerShell):**
```powershell
    $env:GEMINI_API_KEY="your_actual_api_key_here"
    ```

---

## Running the Application

Launch the chatbot by running the main Python script:

```bash
python app.py
Once executed, the terminal will provide a local URL (typically http://127.0.0.1:7860). Open this link in your web browser to start chatting!

Project Structure
Plaintext
├── app.py              # Main application code (Gradio UI + Gemini API integration)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
Technologies Used
Backend: Python

UI Framework: Gradio

LLM API: Google Generative AI SDK (Model: gemini-3-flash-preview)

License
This project is licensed under the MIT License. See the LICENSE file for details.


<ElicitationsGroup message="What would you like to do next?">
<Elicitation label="Create a requirements.txt file matching this setup" query="Create a requirements.txt file matching this setup" />
<Elicitation label="Create the main Python application code using Gradio and Gemini 3 Flash Preview" query="Create the main Python application code using Gradio and Gemini 3 Flash Preview" />
<Elicitation label="Add deployment instructions for Hugging Face Spaces to the README" query="Add deployment instructions for Hugging Face Spaces to the README" />
</ElicitationsGroup>
