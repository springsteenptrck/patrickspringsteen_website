from PIL import Image 
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="my webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- LOAD ASSETS --- 
lottie_coding = "https://lottie.host/1c78344e-9c26-4528-9f48-f01ee42160b8/wVnb2IghU0.json"
img_contact_form = Image.open("images/streamlit_profile_pic.jpg")

# ---- Header Section ---- 
with st.container():
    st.subheader("Hi, I am Patrick :wave:")
    st.title("A Junior Web Developer from Michigan")
    st.write("I am passionate about learning, human physcology, and what makes each individual tick!")
    st.write("[Learn More >](#)")

# ---- What I DO ---- 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            I'm creating this page to expand my understanding of the following:
            - new coding techniques and applications
            - what the strong and weak points of python and other coding languages are 
            - fun
            - to test and retest good strategies for building personalized websites

            If you'd like to watch some of the videos I've posted on Youtube playing and singing, click the link below. 
            """
    )
    st.write("[My  YouTube Channel >](https://www.youtube.com/@pspringsteen100)")

    with right_column:
        st_lottie(lottie_coding, height=300)

#----------PROJECTS -----------

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)

        with text_column:
            st.subheader("Insert Lottie Animations inside your Streamlit App")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our webpage more fun and engaging, 
                and Lottie Files are the easiest way to do it. In this
                tutorial I'm learning exactly how
                """)

#------------ CONTACT ------------

with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!! 
    contact_form = """
    <form action="https://formsubmit.co/springsteenptrck@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    # Use local CSS 
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    local_css("style/style.css")