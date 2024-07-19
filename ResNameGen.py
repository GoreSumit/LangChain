import streamlit as st
st.title("Restaurant Name Generator")
from LangChainHelper import generate_restaurant_name_and_items

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Mexican","Arabic","Italian"))


if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    for i in menu_items:
        st.write("-",i)