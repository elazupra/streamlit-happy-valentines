import json
from pathlib import Path
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

#Directories & File paths
this_dir:Path= Path(__file__).parent
css_file = this_dir / "style" / "style.css"
LOTTIE_ANIMATION = Assets = this_dir /"assets" / "love_birds.json"

#lottie animation display
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

#falling objects
def run_rain_animation():
   rain(emoji="💜" , font_size=20, falling_speed=5, animation_length="infinite")

# page configuration
st.set_page_config(page_title="Lyrica Sandatun", page_icon="💜")

# run falling animation
run_rain_animation()
# Apply custom CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# header with personalized name
st.header(f"Happy Valentines day, Rhea"
          f" Lyrica💜!", anchor=False)

# Lottie animation
lottie_animation =load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-love_birds", height=300)

# personalized message
st.markdown(
    f" Gipalangga ko naman gud ikaw.")


# Create a button
button_clicked = st.button("Sulat for you")

# Check if the button is clicked
if button_clicked:
    # Create a container (box) for the content
    with st.container():
        # Display content inside the container

        st.write("Hi, bibi, Happy Valentines day!")


# Display an image
        image_url = "https://scontent.fdvo2-2.fna.fbcdn.net/v/t39.30808-6/345032242_750430143486236_5165318005415499564_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=dd5e9f&_nc_ohc=nD7tc7TjkUMAX97Pnzr&_nc_ht=scontent.fdvo2-2.fna&oh=00_AfAz9237VRfnThQbGiyTJrtuRCgz_m4zj8IpM1qUzY_gNA&oe=65CDE253 "  # Replace with the URL of your image
        st.image(image_url, caption="pretty mana akong bibi, no need for flowers na 'cause she's the one who is blooming<3", use_column_width=True)

   #personalized message

        st.write(" Dear Lyrica, It's the 14th of February and most people believe that this is a day to express your affection to someone you are inlove with, that's why I coded this website for you and shared it to the world.")

        st.write("No matter what happens, remember that you are loved and cared by those people who value your presense here on earth. So love your life, make it beautiful and be extraordinary<3.  ")

# ------button description ----
button_clicked = st.button("plawers🌼")

        # Check if the button is clicked
if button_clicked:
            # Create a container (box) for the content
            with st.container():
                image_url = "https://i.pinimg.com/736x/79/af/55/79af550b783caac4c9e7a49872fe2712.jpg" 
                st.image(image_url, caption="wild flowers are still flowers, and they too are beautiful",use_column_width=True)

# set the correct pass key
correct_pass_key = "Kandotage"


# Streamlit encrypted message
def main():

    # password input
    entered_pass_key = st.text_input("Exclusive for Lyrica:", type="password")

    # Check if the entered password is correct
   
    if entered_pass_key == correct_pass_key:
       
    #personalized message bar
        st.write("""
   Hi Yang!

   I hope this note finds you well. I've been thinking about you a lot lately, and distance sure does make the heart grow fonder. Life on this end is just the usual routine, but there's a distinct void that only you can fill☺️. 

    I've been keeping myself busy with work and other daily chores, but there's always this constant reminder of you in the background. Your absence makes me appreciate all the hopes where there's you, close to me.

    I hope your days are filled with joy and that you're surrounded by good people. I'm looking forward to the day when we can bridge this gap and create memories together(soon bibi).

""")
 
        st.success(""" Until then, take care, bibi and know that you're missed.

Sending you all my love. """)


        # Add the content that should be displayed upon successful entry
    elif entered_pass_key != "":
        st.error("Password to my heart is incorrect.")


if __name__ == "__main__":
    main()


st.markdown(
    """
    <style>
        div.stTextInput > div > div {
            background-color: #4f3c4b; 
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
