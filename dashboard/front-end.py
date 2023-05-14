# -*- coding: utf-8 -*-
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Marketing project",layout="wide")
# with st.container():
#     left,right=st.columns([11,1])
#     image = Image.open('Logo.jpeg')
#     right.image(image,width=90)   #for this part you need to install pillow module, than uncomment it

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_book= load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_1a8dx7zj.json")


with st.container():
    # left_column, center, right_column=st.columns((1,3,2,3))
    column_widths = [8, 4]

    # Create the columns
    left_column, right_column = st.columns(column_widths)

    with left_column:
        title = "Book Recommendation System"

        wrapped_title = "<br>".join(title.split())

        st.markdown(
            f"""
            <style>
            .title-wrapper {{
                position: relative;
                text-align: left;
                top: 50px; /* adjust to your desired vertical position */
                max-width: 500px; /* adjust to your desired maximum width */
            }}
            .title-wrapper h1 {{
                white-space:pre-line;
                margin: 20px 20px 0 0;
                font-size: 80px;
            }}
            </style>
            <div class="title-wrapper">
                <h1>{wrapped_title}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with right_column:
        st_lottie(lottie_book,height=400, key="book")

    
st.write("##")
with st.container():
    left_column, right_column=st.columns((2,1))
    with left_column:
        text = """<span style='color: #C5C1C1;'>
        Introducing our Book Recommendation System – a powerful tool that can help you discover new books that match your unique reading preferences.
        Our system works by analyzing your inputed text,or inputed book names,its ratings, and other factors to create a personalized profile of your interests. It then uses this profile to make book recommendations that are tailored specifically to you.
        </span>"""
        left_column.markdown(text, unsafe_allow_html=True)

st.write("##")

with st.container():
    left_column, right_column=st.columns((1,2))
    with right_column:
        text = """<span style='color: #C5C1C1;'>
        With our Book Recommendation System, you'll be able to explore a wide range of book genres and authors, including hidden gems and new releases that you may not have discovered otherwise. Whether you're looking for a gripping thriller,
        a heartwarming romance, or an informative non-fiction book, our system has got you covered.
        </span>"""
        right_column.markdown(text, unsafe_allow_html=True)
st.write("##")
with st.container():
    left_column,right_column=st.columns((2,1))
    with left_column:
        text = """<span style='color: #C5C1C1;'>
        Our recommendation algorithm uses advanced machine learning techniques to continuously improve its suggestions over time, based on your feedback and ratings. This means that the more you use our system, the better it gets at recommending books that you'll love.
        So why not try our Book Recommendation System today and discover your next favorite read? Sign up now and start exploring a world of books that are just waiting to be discovered!
        </span>"""
        left_column.markdown(text, unsafe_allow_html=True)

st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")

with st.container():
    st.write("##")
    col1,col2,col3=st.columns((1,2,1))
    # col2.write("Enter a book name or a text for us to give you the best recomendations")
    col2.markdown("<h3 style='text-align: center;'>Click here to start !!</h3>", unsafe_allow_html=True)
    input_style ="""
    <style>
    input[type="text"] {
        border: none;
        text-align: center;
        border-bottom: none;
        transition: border-bottom-color 0.3s ease-in-out;
    }
    input[type="text"]:focus {
        border-bottom-color: #09f;
    }
    </style>
    """
    col2.markdown(input_style, unsafe_allow_html=True)
    search_query = col2.text_input(" ", key='searchbox', placeholder="SEARCH")
    rows = 3
    # search_query = col2.text_area("Enter text here", height=rows,max_chars=None, key=None)
    if col2.button("Search", key='searchbutton', help='Click to perform search', ):
        col2.markdown("""
            <style>
                .css-1aumxhk {
                    display: flex;
                    justify-content: center;
                }
            </style>
        """, unsafe_allow_html=True)
        # Perform the search here
        search_results = perform_search(search_query)
        
        # Display the search results
        col2.write("Search Results:")
        for result in search_results:
            col2.write(result)

st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")


st.write("---")




def footer():
    st.markdown(
        """
        <style>
        footer {
          background-color: #948E8E;
          padding:50px 50px 50px 110px;
        }

        .footer-container {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-between;
        }

        .column {
          width: 45%;
        }
        </style>

        <footer>
        <div class="footer-container">
          <div class="column">
            <h3>About</h3>
            <p>Our Logo <p> ©2023 Company Name .All rights reserved.</p>
          </div>
          <div class="column">
            <h3>Contact Us</h3>
            <p>Phone: +374 (43) 000 000 <p> Emial: info@company.com.</p>
          </div>
        </div>
        </footer>
        """,
        unsafe_allow_html=True,
    )

footer()


    