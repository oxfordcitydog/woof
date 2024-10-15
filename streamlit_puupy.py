import streamlit as st
import pandas as pd

st.title("Oxford City Dog")

# Load data from Excel file
excel_path = 'https://www.dropbox.com/scl/fi/ic6k91cd4n0rev539326r/janesnewform.xlsx?rlkey=fd87gbe96jcgojpvn4vqxhgrp&st=g2wn4r10&dl=0'
try:
    df = pd.read_excel(excel_path, index_col=0)
except FileNotFoundError:
    # Create an empty DataFrame if the file is not found
    df = pd.DataFrame()

st.text("Jane Yates, Streamlit app using Python. Ongoing thing")


# when you use excel make sure you right click and change permission 


# Checkbox section
like_dogs = st.checkbox("Do you like dogs?")
like_cats = st.checkbox("Do you like cats?")
like_dogs_and_like_cats = st.checkbox("Do you like dogs and cats?")
button2 = st.button("Submit")

if button2:
    # Check if none of the options are selected
    if not (like_dogs or like_cats or like_dogs_and_like_cats):
        st.write("Oh, you don't like dogs or cats?")
    else:
        # Create a new DataFrame with the new entry
        new_entry = {'Like Dogs': [like_dogs], 'Like Cats': [like_cats], 'Like Dogs and Cats': [like_dogs_and_like_cats]}
        new_df = pd.DataFrame(new_entry)
        
        # Append the new DataFrame to the existing DataFrame
        df = pd.concat([df, new_df], ignore_index=True)
        
        # Save the updated DataFrame back to the Excel file
        df.to_excel(excel_path, index=True)

        # Display a success message
        st.success("Data submitted successfully!")

        # Customized response based on the user's preference for dogs
        if like_dogs:
            st.write("That's fantastic! Since you like dogs, you're in the right place. This app is all about dogs.")
        if like_cats:
            st.write("That's a shame this site's all about dogs.") 
        if like_dogs_and_like_cats:
            st.write("Cool, you like dogs.")
# ... (rest of your code remains unchanged)

