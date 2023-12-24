import streamlit as st
from streamlit_option_menu import option_menu

import about, prop, arim

st.set_page_config(
    page_title = "Dashboard"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run():
        with st.sidebar:
            app = option_menu(
            menu_title = "GOLD Prediction", 
            options = ["About Project", "PROPHET Model", "ARIMA Model"],
            icons = ["clipboard2-fill","graph-up-arrow", "graph-up-arrow" ],
            menu_icon = "grid-fill",
        )
            
        if app == "About Project":
            about.app()
        if app == "PROPHET Model":
            prop.app()
        if app == "ARIMA Model":
            arim.app()
    
    run()