import streamlit as st
import re

st.set_page_config(page_title="Text Analyzer", layout="wide")

st.title("Text Analyzer 📈")
st.write("This app will analyze your paragraph and give you some informative stats about the paragraph")

st.markdown("<h3 style=color:Khaki;>Enter your paragraph below </h3>",unsafe_allow_html= True)


if "text_input" not in st.session_state:
    st.session_state.text_input = ""


text = st.text_input("",key="text_input")


def analyzer(text):

    st.markdown("<h3 style=color:Khaki;>Paragraph analysis </h3>",unsafe_allow_html= True)

    wordCount = len(re.findall(r"\b\w+\b",text))
    st.subheader(f"The number of words in the paragraph are : {wordCount}")

    number = len(text.strip())
    st.subheader(f"The number of characters in the paragraph are : {str(number)}")

    vowel = len(re.findall(r"[AEIOUaeiou]",text))
    st.subheader(f"The number of vowels in the paragraph are : {str(vowel)}")

    spaces = len(re.findall(r"\s",text))

    if wordCount != 0:
        avg = (number-spaces)/wordCount
        st.subheader(f"The average word length of the paragraph is : {avg}")
    else:
        st.subheader(f"The average word length of the paragraph is 0")


    if any(w == "python" for w in text.lower().split()):
        st.subheader(" The word python exists")

    st.markdown("<h3 style=color:Khaki;>Paragraph in upper and lower case</h3>",unsafe_allow_html= True)
    st.text(text.upper())
    st.text(text.lower())



def replace():

    st.markdown("<h3 style=color:Khaki;>Find and Replace word</h3>",unsafe_allow_html= True)

    if "replace_word" not in st.session_state:
        st.session_state.replace_word = ""

    if "current_word" not in st.session_state:
        st.session_state.current_word = ""

    
    currentWord = st.text_input("Enter the word from the paragraph to replace with (case sensitive)",key="current_word")

    replaceWord = st.text_input("Enter the word to replace",key="replace_word")
    

    if replaceWord and currentWord:
        
        if currentWord in text:
            new_text = text.replace(currentWord,replaceWord)
            st.subheader(new_text)
        else:
            st.warning("Word not found")

    else:
        st.warning("Above fields are required")



if st.session_state.text_input.strip():
    analyzer(text)
    replace()
else:
    st.warning("Please enter some text to analyze.")
