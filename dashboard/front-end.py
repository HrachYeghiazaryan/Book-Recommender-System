# -*- coding: utf-8 -*-
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
# from search import search_books
from perform_search import perform_search
import argparse
import numpy as np
import pandas as pd
import spacy
from googletrans import Translator
import os


st.set_page_config(page_title="Marketing project",layout="wide", initial_sidebar_state='auto')
# st.markdown('<link rel="stylesheet" type="text/css" href="./assets/style.css">', unsafe_allow_html=True)

shape_style = """

<style>
.rectangular-shape {

    background-color: #948E8E;
    border: 3px solid #d3d3d3;
    padding: 20px;
    bottom: 0;
    left: 100;
    width: 100%;
    width: 1000px
} </style>
"""
with st.container():
    with st.container():
        left,right=st.columns([11,1])
        image = Image.open('Logo.jpg')
        right.image(image,width=90)
   


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
                    top: 10px; /* adjust to your desired vertical position */
                    left: 20px;
                    max-width: 600px; /* adjust to your desired maximum width */
                }}
                .title-wrapper h1 {{
                    white-space:pre-line;
                    margin: 10px 20px 0 0;
                    font-size: 82px;
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
            text = """<span style='color: #C5C1C1;font-size: 20px;'>
            – A powerful tool that helps you discover books that match your unique reading preferences.
            Our system works by analyzing your inputed text,or inputed book names,its ratings. With our Book Recommendation System, you'll be able to explore a wide range of book genres and authors,
            including hidden gems and new releases that you may not have discovered otherwise.</span>"""
            left_column.markdown(text, unsafe_allow_html=True)

    st.write("##")
    with st.container():
        text = """<span style='color: #C5C1C1;font-size: 20px;'>
        - Our recommendation algorithm uses advanced machine learning techniques to continuously improve its suggestions over time, based on your feedback and ratings. This means that the more you use our system, the better it gets at recommending books that you'll love.
        So why not try our Book Recommendation System today and discover your next favorite read? Sign up now and start exploring a world of books that are just waiting to be discovered!
        </span>"""
        st.markdown(text, unsafe_allow_html=True)
    st.write("##")



with st.container():    
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")



with st.container():
    def search_function():
        
        parser = argparse.ArgumentParser()
        parser.add_argument('-embeddings_dir_name', type=str, default=  r"zangak_embeddings_pq", help='the name of the directory to use embeddings from')
        parser.add_argument('-num_similars', type=int, default = 10, help='the number of most similar books to keep')
        args = parser.parse_args()

        st.write("##")
        col1, col2, col3 = st.columns((1,2,1))
        # col2.markdown("<h3 style='text-align: center;font-size: 40px; color: #C5C1C1'>Click here to start !!</h3>", unsafe_allow_html=True)
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
        # user_query = st.text_input(label="Enter query")
        prev_qry = " "
        
        col2.markdown("""
            <style>
                .css-6dnr6u {
                    display: flex;
                    justify-content: center;
                    left:100;
                }
            </style>
        """, unsafe_allow_html=True)

        if col2.button("Search", key='searchbutton', help='Click to perform search') or (prev_qry != search_query):
            if search_query.strip():  # check if search_query is not an empty string
                prev_qry = search_query

                # Perform the search here
                search_results = perform_search(search_query, args.embeddings_dir_name)

                col1, col2, col3 = st.columns([2,6,4])

                shape_style = """
                <style>
                    .rectangular-shape {
                        background-color: #D9D9D9;
                        border: 10px solid #A9A9B6;
                        padding: 10px;
                        bottom: 0;
                        width: 100%;
                        width: 850px;
                        color: #000235;
                        font-weight: bold;
                    }
                </style>
                """

                col2.markdown(shape_style, unsafe_allow_html=True)

                # Display the search results
                col2.markdown('<div class="rectangular-shape" style="text-align: center; border: 10px; text-decoration: none; border-bottom_style: none; font-size: 30px"> Search Results: </div>', unsafe_allow_html=True)
                result_list = []
                for line in search_results:
                    result_list.append(line)
                    col2.markdown(f'<div class="rectangular-shape"> {line}</div> ', unsafe_allow_html=True)
                    # col1.markdown(f'<a href="{line}" target="_blank" style="color: #FF5733;">{line}</a>', unsafe_allow_html=True)
                return result_list


            

    if __name__ == '__main__':
        with st.container():
            search_function()

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
            background-color: #D9D9D9;
            padding:50px 50px 50px 110px;
            font-size: 20px;
            }

            .footer-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            }
            .footer-container p {
            color: #000000;
            font-size: 20px;
            }

            .column {
            width: 45%;
            }
            h3 {
            color: #000000;
            }
            
            </style>

            <footer>
            <div class="footer-container">
            <div class="column">
                <h3>About</h3>
                <p>  <p>  <p>  <p>  <p> <p>  <p> <p>  <p> Our Logo <p> ©2023 Company Name .All rights reserved.</p>
            </div>
            <div class="column">
                <h3>Contact Us</h3>
                <p>Phone: +374 (43) 000 000  <p> ----- +374 (43) 000 000 <p> ----- +374 (43) 000 000 <p> Emial: info@company.com. <p> ----- info@company.com.<p> ----- info@company.com. </p>
            </div>
            </div>
            </footer>
            """,
         unsafe_allow_html=True,
    )

footer()


        