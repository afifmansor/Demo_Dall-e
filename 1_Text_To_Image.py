import streamlit as st
import openai
from security_utils import check_password

# Access the OpenAI API key
openai.api_key = st.secrets["api_key"]

# configure the default settings of the page.
st.set_page_config(
                layout="wide",
                initial_sidebar_state="expanded"
                )

if check_password():
    st.title('IdeaSpark DALL-E Image Generation')
    st.info(""" NOTE: You can download image by\
                    right clicking on the image and select save image as option""")  

    # Create the form
    with st.form(key="image_form"):
                # Text input for the image prompt
                prompt = st.text_input(label="Enter the image prompt")

                # Select box to select the size of the images
                size = st.selectbox(label="Select the size of the images", options=["256x256", "512x512", "1024x1024"])

                # Number input to specify the number of images to be generated
                num_images = st.selectbox("Enter the number of images to be generated", (1,2,3,4))

                # Submit button
                submit_button = st.form_submit_button(label="Generate Images")

    # Handle form submission
    if submit_button:
                # TODO: Add code to generate images using the specified prompt, size, and number of images
                if prompt:
                    response = openai.Image.create(
                            prompt = prompt,
                            n = num_images,
                            size=size,
                        )
                    
                    for idx in range(num_images):
                        image_url = response['data'][idx]['url']

                        st.image(image_url, caption=f'Generated image: {idx+1}',
                                use_column_width=True)                               



