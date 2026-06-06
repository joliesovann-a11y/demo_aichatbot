import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API"))
model = genai.GenerativeModel('gemini-3-flash-preview')

conversation_history = []

def chat(message, history):
    conversation_history.append({"role": "user", "parts": [message]})
    try:
        response = model.generate_content(conversation_history)
        conversation_history.append({"role": "model", "parts": [response.text]})
        return response.text
    except Exception as e:
        conversation_history.pop()  # Remove the failed user message
        return f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=chat,
    title="Jolie AI Chatbot",
    description="Ask anything you want",
    examples=["Hello", "What is Python", "What happens in Middle East?"],
    
)
demo.launch(share=True)
