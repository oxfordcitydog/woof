#this is a new file about exploring streamlit elements - first bring in the streamlit library
import streamlit as st

#st dot Displays text in Streamlit
st.text("Link to my Blog")
# link to my blog
st.markdown('[OxfordCityDog.com](http://oxfordcitydog.com)')

#to check code save it, then run it by hitting windows key + X, terminal. call the file and directory


# Define the relative widths of the columns
column_widths = [1, 2, 3]

import streamlit as st
from PIL import Image

# Create a list to store uploaded photos
uploaded_photos = []

# Create three columns with specified widths
col1, col2, col3 = st.columns([1, 2, 3])

# Add Markdown content to col1 (1/6 width) without showing the header
col1.markdown('# Welcome to Woof!')
col1.markdown('This is a woof-tastic page.')

# Add Markdown content to col2 (1/3 width)


# Upload a photo in col3 (1/2 width)
new_photo = col3.file_uploader('Upload a photo of your dog 🐾', type=['jpg', 'png', 'jpeg'])
if new_photo is not None:
    uploaded_photos.append(new_photo)

# Display all uploaded photos in col3
for i, photo in enumerate(uploaded_photos):
    col3.image(Image.open(photo), caption=f'Uploaded Photo {i+1}', use_column_width=True)

