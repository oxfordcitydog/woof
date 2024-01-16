# Importing necessary libraries
import streamlit as st

# Page title
st.title("Exploring Streamlit Metrics")

# Add a brief description or introduction
"""
In this application, we'll explore various Streamlit metrics for visualization and analysis.
"""

# Now, let's start by adding some widgets or visual elements.

# Create two columns
col1, col2 = st.columns(2)

# Add a metric in the first column
with col1:
    # Displaying temperature metric
    st.metric(label='Temperature', value='60 degrees', delta='3 degrees')
# Create an expander
expander = st.expander("Click to read more")

# Inside the expander, provide more details including text and image
with expander:
    # Additional text details
    st.write("This is the additional information or more details that you can reveal by clicking the expander.")

    # Display an image from the internet (replace URL with your image URL)
    image_url = 'https://i0.wp.com/oxfordcitydog.com/wp-content/uploads/2023/03/oak-plaiun375.jpg?w=375&ssl=1'
    st.image(image_url, caption='Oak from Oxford City Dog', use_column_width=True)




