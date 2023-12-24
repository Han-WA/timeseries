import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from prophet import Prophet
from datetime import datetime

def app():
    st.title("About Project")

    mydata = pd.read_csv(r"D:\dashboard\xauusd_d.csv")

    about = '''This project involves the analysis and forecasting of gold prices using a dataset obtained from stooq.com.
    The dataset spans from January 1, 2010, to the current date in December. 
    Gold has long been a pivotal asset in the financial markets, and forecasting its price trends is crucial for various stakeholders.
    '''
    st.markdown(about)
    st.markdown("##")
    st.markdown("##")

    # Printing the dataswet shape
    st.subheader('Gold Price Dataset')
    mydata
    st.markdown("##")
    st.markdown("##")

    st.header("Gold price line chart with Plotly")
    line1 = px.line(mydata, x= mydata['Date'] , y=mydata['Close'])
    line1.update_xaxes(rangeslider_visible=True)
    st.plotly_chart(line1,use_container_width=True)
    st.markdown("##")
    st.markdown("##")

    st.header("Area Chart")
    st.caption("Compare the open, high, low, and close prices for a specific date or time period.")
    fig_area = px.area(mydata, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Cumulative Gold Prices', labels={'value': 'Cumulative Price'})
    st.plotly_chart(fig_area)
    st.markdown("##")
    st.markdown("##")

    st.header("Scatter Plot")
    st.caption("Show the relationship between two variables, such as open and close prices.")
    fig_scatter = px.scatter(mydata, x='Open', y='Close', title='Scatter Plot of Open vs. Close Prices')
    st.plotly_chart(fig_scatter)
    st.markdown("##")
    st.markdown("##")

    st.header("Histogram")
    st.caption("Display the distribution of a single variable, like the daily price changes.")
    mydata['Price Change'] = mydata['Close'] - mydata['Open']
    fig_hist = px.histogram(mydata, x='Price Change', title='Distribution of Daily Price Changes')
    st.plotly_chart(fig_hist)
    st.markdown("##")
    st.markdown("##")

    st.header("Box Plot")
    st.caption("Visualize the distribution of the open, high, low, and close prices.")
    fig_box = px.box(mydata, y=['Open', 'High', 'Low', 'Close'], title='Box Plot of Gold Prices')
    st.plotly_chart(fig_box)
    st.markdown("##")
    st.markdown("##")



