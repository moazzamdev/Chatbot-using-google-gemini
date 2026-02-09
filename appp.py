import streamlit as st
from streamlit_option_menu import option_menu
from page1 import text
from page2 import image
import openai
def main():

    st.title("Chat With Gemini")

    with st.sidebar:
        selection = option_menu(
        menu_title="Main Menu",
        options=["Text Model", "Image Model"],
        icons=["pencil", "image"],
        menu_icon="cast",
        default_index=0
        )

    if selection == "Text Model":
        text()

    elif selection == "Image Model":
        image()


if __name__ == '__main__':
    main()

