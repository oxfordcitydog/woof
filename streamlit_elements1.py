#this is a new file about exploring streamlit elements - first bring in the streamlit library
import streamlit as st

# Displays text in Streamlit
st.text("Link to my Blog")

# Link to my blog
st.markdown('[OxfordCityDog.com](http://oxfordcitydog.com)')

# Define the relative widths of the columns
column_widths = [1, 1, 1]

# Create a list to store uploaded photos
uploaded_photos = []

# Create three columns with specified widths
col1, col2, col3 = st.columns([1/3, 1/3, 1/3])

# Add Markdown content to col1 (1/6 width) without showing the header
col1.markdown('# Welcome to Woof!')
col1.markdown('This is a woof-tastic page.')

# Add Markdown content to col2 (1/3 width)
col2.markdown('images by jane and AI')

# Display the image
# Image URL
image_url = "https://i0.wp.com/oxfordcitydog.com/wp-content/uploads/2024/01/DALL%C2%B7E-2024-01-04-18.20.59-3d-rendered-of-a-yellow-balloon-dog-on-pale-green-background.png?resize=300%2C300&ssl=1"
st.image(image_url, caption='Woof', use_column_width=True)
#end of this bit of code

# Upload a photo in col3 (1/2 width)
new_photo = col3.file_uploader('Upload a photo of your dog 🐾', type=['jpg', 'png', 'jpeg'])
if new_photo is not None:
    uploaded_photos.append(new_photo)

# Display all uploaded photos in col3
for i, photo in enumerate(uploaded_photos):
    col3.image(Image.open(photo), caption=f'Uploaded Photo {i+1}', use_column_width=True)

from calendar import EPOCH
from curses import BUTTON3_CLICKED, BUTTON4_CLICKED
import streamlit as st
st.title("My Name is Jane Yates, I a working on this streamlit app using python, its an ongoing thing")


# Checkbox section
like_dogs = st.checkbox("Do you like dogs?")
like_cats = st.checkbox("Do you like cats?")
button2 = st.button("Submit")

if button2:
    if like_dogs and like_cats:
        st.write("Great, you like both dogs and cats!")

    elif like_dogs:
        st.write("Great, you like dogs! your in the right place, this app is all about dogs")

    elif like_cats:
        st.write("You like cats! sorry this apps all about dogs")

    else:
        st.write("Oh, you're not a fan of dogs or cats? I'm sorry")
    
#radio section
#st.write("This is a radio button section")
st.title("What is your favorite dog?")
dog = st.radio("Choose your favorite dog?", ("Labrador", "Spaniel", "Sausage Dog","Other"))
button3 = st.button("Submit Dog")

if button3:
    st.write(dog)

    if dog == "Spaniel":
        st.write("Woof! Woof!")

    if dog == "Sausage Dog":
        st.write("Woof! Woof! Woof!")
    if dog == "Other": 
        st.write("To be fair, there are so many other dogs in the world.")   
#box section  
    
#st.write("This is a box section")
st.title("What is your favorite dog food?")
dogfood = st.selectbox("Choose your favorite dog food?", ("Kibble", "Tin", "Home Cooked", "Other",))
button4 = st.button("Submit dog food")
if button4:
    st.write(dogfood)
if dogfood == "Kibble":
    st.write("Kibble is nice!")
if dogfood == "Tin":
    st.write("Yummy!")
if dogfood == "Home Cooked":
    st.write("Home Cooked is tasty!")
if dogfood == "Other": 
    st.write("To be fair, there are so many other dog food in the world.") 



# Dropdown multiple selection
st.title("Where is your favorite place to walk your dog?")
options = st.multiselect("Choose your order of favorite place to walk your dog?", ("Park", "River side", "Other",))

button5 = st.button("Print your walk")
st.write(options)  # Display the selected options

if button5:
    if not options:
        st.write("Please select at least one option.")
    else:
        st.write("You selected:", options)

        if len(options) == 1:
            st.write("You have one favorite place to walk your dog.")
        elif len(options) == 2:
            st.write("You have two favorite places to walk your dog.")
        else:
            st.write(f"You have {len(options)} favorite places to walk your dog.")

        if "Park" in options:
            st.write("Park is one of your favorite places to walk your dog")

        if "River side" in options:
            st.write("River side is one of your favorite places to walk your dog")

        if "Other" in options:
            st.write("To be fair, there are so many other places to walk your dog")




#give epoch a number, that allows you to select a number of dogs in seghments, like 1, or 10, or 100

EPOCH = 1

# Slider section
st.header("What number of dogs do you have?")
EPOCH_num = st.slider("Choose number of your dogs", min_value=EPOCH, max_value=10, value=1, step=1)
button6 = st.button("Submit number")

if button6:
    if EPOCH_num == 1:
        st.write("You have 1 dog. That's great!")

    elif EPOCH_num > 1:
        st.write(f"You have {EPOCH_num} dogs. Wow, that's a lot of dog friends! Lucky you")

    else:
        st.write("Please select a valid number of dogs.")
        


# New section asking about dog-friendly places in Oxfordshire
# Make a text box
st.header("What's the most dog-friendly place you have been in Oxfordshire?")
user_text = st.text_input("What is your favorite place to go with your dog?")
button7 = st.button("Submit text", key="submit_text_button")

if button7:
    st.write(user_text)

# Make a number box with a range from 1 to 5
st.header("How much would you rate it for dog-friendliness?")
user_number = st.number_input("Rate out of 5?", min_value=1, max_value=5)
button8 = st.button("Submit number", key="submit_number_button")

if button8:
    st.write(user_number)






