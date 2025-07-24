import streamlit as st
from openai import OpenAI
from prompts import get_questions_prompt
from questions import generate_questions
from utils import validate_email, validate_phone

st.set_page_config(page_title="TalentScout Hiring Assistant")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://protoverify.com/wp-content/uploads/2023/07/The-Benefits-of-AI-in-Conducting-Rapid-Background-Checks.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🤖 TalentScout: AI Hiring Assistant")

if "questions" not in st.session_state:
    st.session_state.questions = []

exit_keywords = ["exit", "quit", "bye"]

def check_exit(user_input):
    if any(k in user_input.lower() for k in exit_keywords):
        st.write("👋 Thank you for your time.")
        st.stop()

def main():
    with st.form("candidate_form"):
        st.subheader("📝 Candidate Information Form")

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
        stack = st.text_area("Tech Stack (comma-separated)")

        submit = st.form_submit_button("Submit & Generate Questions")

    if submit:
        for field in [name, email, phone, experience, position, location, stack]:
            check_exit(field)

        if not validate_email(email):
            st.error("Please enter a valid email address.")
            return
        if not validate_phone(phone):
            st.error("Please enter a valid phone number.")
            return
        if not experience.isdigit():
            st.error("Experience must be a number.")
            return

        st.session_state.user_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "experience": experience,
            "position": position,
            "location": location,
            "stack": stack,
        }

        st.session_state.questions = generate_questions(stack)

    if st.session_state.questions:
        st.subheader("📋 Your Custom Technical Questions:")
        for i, q in enumerate(st.session_state.questions, 1):
            st.markdown(f"**Q{i}.** {q}")
        st.success("✅ Thank you! We'll reach out with the next steps shortly.")

main()


def get_info_prompt():
    return "You are a smart hiring assistant. Ask the candidate for: Full Name, Email, Phone Number, Experience, Desired Position, Location, and Tech Stack."

def get_questions_prompt(stack):
    return f"Generate 3-5 technical interview questions for each of these technologies: {stack}. Questions should assess the candidate's proficiency."
            
    
    