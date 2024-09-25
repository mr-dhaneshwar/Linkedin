import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyAZRkCgSxW0YHo8GcGvqRnLBL9Sf8oAC3E")

# Model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Function to create a prompt based on user input
def create_prompt(topic, use_hashtags, use_emojis, use_bullets, description):
    prompt = f"Create a LinkedIn caption on the topic '{topic}'"
    
    if use_hashtags:
        prompt += " using relevant hashtags."
    else:
        prompt += " don't using any hashtags it is sticctly prohabited."
    if use_emojis:
        prompt += " with appropriate emojis."
    else:
        prompt += " don't using any emojis it is sticctly prohabited."
    if use_bullets:
        prompt += " and use bullet points to organize the content."
    else:
        prompt += " and no need to use bullet points  it is also sticctly prohabited."
    
    prompt += f" Description for the post: {description}."
    prompt += " The caption should be professional, engaging, and optimized for LinkedIn."
    return prompt

# Function to interact with the Gemini API and generate a response
def angel(prompt):
    # Instantiate the model
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    # Start the conversation and send the prompt
    convo = model.start_chat(history=[])
    convo.send_message(prompt)

    # Retrieve the last message from the conversation
    message = convo.last.text
    return message

# Streamlit UI
st.title("LinkedIn Caption Generator")

# Input fields
topic = st.text_input("Enter the Topic of the Post")
use_hashtags = st.checkbox("Use Hashtags")
use_emojis = st.checkbox("Use Emojis")
use_bullets = st.checkbox("Use Bullet Points")
description = st.text_area("Enter the Description of the Post")

# Initialize the caption variable
generated_caption = ""

# Button to generate caption
if st.button("Generate Caption"):
    # Create prompt based on inputs
    prompt = create_prompt(topic, use_hashtags, use_emojis, use_bullets, description)
    
    # Generate caption using the Gemini API
    generated_caption = angel(prompt)

# Display the generated caption in a text area
if generated_caption:
    st.text_area("Generated Caption", value=generated_caption, height=200, key="caption_area")
