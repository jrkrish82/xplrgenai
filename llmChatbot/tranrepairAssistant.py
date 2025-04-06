import os
from dotenv import load_dotenv
import streamlit as st
import re
from ollama import chat, ChatResponse, Options


#MODEL_NAME = "deepseek-r1:1.5b"
MODEL_NAME = "llama2:7b"

def get_completion(prompt: str, system_prompt=""):
    response = chat(
        model=MODEL_NAME,
        options=Options(
            max_tokens=2000,
            temperature=0.0
        ),
        messages=[
            {"role": "system", "content": system_prompt},  
            {"role": "user", "content": prompt}
        ]
    )
    return response.message.content

st.title("AI Chatbot")
# If the Global variable is not created, create it once.
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Parse through the Global and print the Chat History
for chats in st.session_state.chat_history:
    with st.chat_message(chats["role"]):
        st.markdown(chats['content'])



if user_input := st.chat_input("........"):
    # Print User Input
    with st.chat_message("User"):
        st.markdown(user_input)
        # Store the User input in Streamlit Global
        st.session_state.chat_history.append({"role":"User", "content": user_input})

    ############################## Instruction to LLM, Constant msg most of the time ###############################
    system_msg = {
        "role": "system",
        "content": (
            "You are a highly skilled payment transaction repair specialist. Your role is to assist users in identifying, diagnosing, and resolving issues related to payment transactions. "
            "Ask clarifying questions if needed, provide step-by-step solutions, and ensure your responses are accurate, professional, and easy to understand. "
            "If the issue involves sensitive information, remind users not to share confidential details like full credit card numbers or passwords."
        )
    }
    
    ###################################### Variable Input Query to LLM ################################################
    user_msg   = {
                    "role"      : "user", 
                    "content"   : f"'''User Query:'{user_input}''''"
                }

    ######################################## Prompt ##########################################
    prompt      = [system_msg, user_msg]

    #################################### AI invoking ########################################################
    llm_response = get_completion(prompt=prompt[1]["content"], system_prompt=prompt[0]["content"])
    # Print the AI Response
    print("AI Response: ", llm_response)
    
    
    
    # Print AI Response
    with st.chat_message("Assistant"):
        st.markdown(llm_response)
        # Store the AI Response in Streamlit Global
        st.session_state.chat_history.append({"role":"Assistant", "content": llm_response})