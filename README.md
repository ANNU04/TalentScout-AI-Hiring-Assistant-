# TalentScout-AI-Hiring-Assistant-
# 🧠 Hiring Assistant Chatbot – TalentScout

An AI-powered Hiring Assistant chatbot built with **Python** and **Streamlit**, designed to streamline the candidate screening process by asking relevant background and technical questions in real time.

---

## 🚀 Project Overview

**TalentScout** is a smart Hiring Assistant chatbot that helps recruiters and hiring managers evaluate candidates efficiently. The chatbot:
- Interacts with candidates to gather background information (education, experience, skills).
- Asks relevant technical questions based on the user's skill stack.
- Stores conversation history and responses.
- Provides a structured interface for candidate assessment.

This project is ideal for companies aiming to automate early-stage interviews or internal candidate assessments using AI.

---

## 🛠️ Installation Instructions

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### 1. Clone the Repository
git clone https://github.com/yourusername/hiring-assistant-chatbot.git
cd hiring-assistant-chatbot

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Add OpenAI API Key
OPENAI_API_KEY=your_api_key_here

### 4. Run the app
streamlit run app.py

### 5. Usage Guide
Launch the Streamlit app.

a. Enter your name and stack (skills like Python, React, etc.).

b. The chatbot will:

c. Ask background questions.

d. Generate technical questions dynamically based on your stack.

e. Please submit your answers using a clean form interface.

f. Recruiters can review conversation history and candidate responses.

### 6. Technical Details
Libraries Used

a. streamlit – for building the UI

b. OpenAI – for generating prompts and handling conversations

c. dotenv – for managing environment variables

d. pandas – for structured data handling (optional)

e. uuid – for generating unique user sessions

### 7. Model Details
OpenAI's gpt-3.5-turbo or gpt-4 model is used for generating prompts and evaluating responses.

### 8. Architecture

a. Modular structure with separate files for prompts, question generation, and session state.

b. Prompt chaining logic based on candidate input.

c. All user inputs are managed through Streamlit forms and session state.

### 9. Prompt Design
Prompts are carefully crafted to achieve:

a. Natural candidate interaction.

b. Context-aware technical question generation.

c. Dynamic prompt chaining (e.g., ask technical questions only after collecting the stack).

### 10. Challenges & Solutions

a. Quota Limit with OpenAI API: Implemented retry logic and modular prompt structure to minimize token usage.

b. Maintaining conversation context:	Used Streamlit's session_state to persist chat history and user responses.

c. Form reloading and state management:	Built separate input submission handlers to prevent data loss during reruns.

d. Styling background images and form opacity:	Used inline HTML & CSS within Streamlit markdown blocks to customize UI.

