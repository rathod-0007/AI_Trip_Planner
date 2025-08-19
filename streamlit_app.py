import streamlit as st
import requests
import datetime

# Backend FastAPI endpoint
backend_url = "http://localhost:8000/query"

st.set_page_config(
    page_title="Travel Planner Agentic Application",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🌍 Travel Planner Agentic Application")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("How can I help you in planning a trip? Let me know where do you want to visit.")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("User Input", placeholder="e.g. Plan a trip to Goa for 5 days")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        with st.spinner("Bot is thinking..."):
            payload = {"question": user_input}
            response = requests.post(backend_url, json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")

            # Save user query and bot response to chat history
            st.session_state.messages.append({
                "query": user_input,
                "answer": answer,
                "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            })

        else:
            st.error("❌ Bot failed to respond: " + response.text)

    except Exception as e:
        st.error(f"⚠️ The response failed due to: {e}")

# Render chat history
if st.session_state.messages:
    st.subheader("📜 Chat History")
    for msg in reversed(st.session_state.messages):  # latest first
        st.markdown(f"""
        **🧑 You:** {msg['query']}  
        **🤖 Bot:** {msg['answer']}  
        ⏰ *{msg['timestamp']}*  
        ---
        """)
