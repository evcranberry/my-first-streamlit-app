import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import yfinance as yf
import io

st.write('''
         # Данные о котировках Apple
         с использованием библиотеки ___yfinance___
         ''')

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2014-12-16', end='2024-12-16')

st.write('''
## Цена открытия
''')
st.line_chart(tickerDf.Open)

st.write('''
## Цена закрытия
''')
st.line_chart(tickerDf.Close)

st.write('''
## Максимальная цена
''')
st.line_chart(tickerDf.High)

st.write('''
## Минимальная цена
''')
st.line_chart(tickerDf.Low)

st.write('''
## Объём торгов
''')
st.line_chart(tickerDf.Volume)

