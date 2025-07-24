import streamlit as st
from openai import OpenAI
from prompts import get_questions_prompt

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_questions(stack):
    prompt = get_questions_prompt(stack)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        questions = [q.strip("-• ") for q in content.strip().split("\n") if q.strip()]
        return questions
    except Exception as e:
        st.error(f"❌ OpenAI Error: {e}")
        return ["Error generating questions. Please try again later."]

