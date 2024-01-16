import streamlit as st
import pandas as pd

st.title("Data Entry Form")

# Load data from Excel file
excel_path = 'C:\\Users\\janey\\Documents\\Data\\janesworkbook.xlsx'
try:
    df = pd.read_excel(excel_path, index_col=0)
except FileNotFoundError:
    # Create an empty DataFrame if the file is not found
    df = pd.DataFrame()

# Streamlit UI for user input
st.header("Enter Data:")
human_name = st.text_input("Human Name:")
email_address = st.text_input("Email Address:")
dogs_name = st.text_input("Dog's Name:")

# Button to submit the form
if st.button("Submit"):
    # Create a new DataFrame with the new entry
    new_entry = {'Human Name': [human_name], 'Email Address': [email_address], 'Dogs Name': [dogs_name]}
    new_df = pd.DataFrame(new_entry)
    
    # Append the new DataFrame to the existing DataFrame
    df = pd.concat([df, new_df], ignore_index=True)
    
    # Save the updated DataFrame back to the Excel file
    df.to_excel(excel_path, index=True)

    # Display a success message
    st.success("Data submitted successfully!")

# Optionally display the loaded and updated data (commented out by default)
# st.write("Data from Excel:")
# st.write(df)
# st.write("Updated Data:")
# st.write(df)
