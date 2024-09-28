import streamlit as st
from genrate import*


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
