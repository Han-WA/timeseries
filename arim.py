import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime
from pandas import DataFrame
import numpy as np

dataset = pd.read_csv(r"D:\dashboard\xauusd_d.csv")

df = pd.DataFrame(dataset)

train_data = df[0:int(len(df)*1)]
training_data = train_data["Close"].values

start_date = '2022-12-30'

histroy = [x for x in training_data]


def app():
    st.title("ARIMA Model")

    pre_day = st.number_input("Select Day", min_value=1, max_value=31, value=1)
    pre_month = st.number_input("Select Month", min_value=1, max_value=12, value=1)
    pre_year = st.number_input("Select Year", min_value=2023, max_value=2025, value=2023)
    futuretime = list()
    model_predictions = []

    day = str(pre_day)
    year = str(pre_year)
    month = "%02d" % pre_month

    end_date = year + '-' + month + "-" + day

    date_range = pd.date_range(start=start_date, end=end_date)

    weekdayonly = date_range[date_range.to_series().dt.dayofweek < 5]
    daysinbetween = len(weekdayonly)

    if pre_year == 2024 and pre_month == 2:
        for k in range(1, 30):
            year_month_date = year + '-' + month + '-' +'%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    elif pre_month == 2:
        for k in range(1, 29):
            year_month_date = year + '-' + month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    elif pre_month == 9 or pre_month == 4 or pre_month == 6 or pre_month == 11:
        for k in range(1, 31):
            year_month_date = year + '-' + month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    else:
        for k in range(1, 31):
            year_month_date = year + '-' + month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    
    futuretime = pd.DataFrame(futuretime)
    futuretime.columns = ['ds']

    for i in range(daysinbetween + len(futuretime)):
        model = ARIMA(histroy, order = [0,1,0])
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        histroy.append(yhat)
        if i >= len(futuretime):
            model_predictions.append(yhat)

    st.subheader("Higher Confidence Interval" + "-" + str(model_predictions[0]+277.0296785004965))
    st.subheader("Prediction price for the day" + "-" + str(model_predictions))
    st.subheader("Lower Confidence Interval" + "-" + str(model_predictions[0]-277.0296785004965))

    # combined_data = futuretime.merge(model_predictions, left_on='ds', right_on='yhat')
    # st.dataframe(combined_data)