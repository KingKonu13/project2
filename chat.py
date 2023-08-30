import openai
import os
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = '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' 

def generate_response(text):  # function that generates AI responses
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ]
    )
    return response['choices'][0]['message']['content']

def get_text():  # Function that takes in user input 
    input_text = st.text_input("", key="input_text")  # renders input on the front end 
    return input_text

if 'past' not in st.session_state:  # stores inputs from the user in a dictionary
    st.session_state['past'] = []  # User Given Text

if 'generated' not in st.session_state:  # stores responses from the AI in a dictionary 
    st.session_state['generated'] = []  # AI Generated Text

def main():  # frontend
    st.title('Personal Chat Bot')  # User Given Text

    user_input = get_text()

    if user_input:
        response = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(response)

    if st.session_state['generated']:  # if session state is initialized then display every AI and User gen messages
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True)
            message(st.session_state['generated'][i])

if __name__ == '__main__':
    main()
