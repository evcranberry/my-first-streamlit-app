import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import plotly.express as px

st.title('__Загрузите файл tips.csv__')


uploaded_file = st.file_uploader(label='Загружать файл сюда:', type='csv')
if uploaded_file is not None:
    tips = pd.read_csv(uploaded_file)
    st.write('Теперь можете выбрать необходимую аналитику в _боковом меню_')
else:
    st.stop()
df = tips.drop(columns='Unnamed: 0', inplace=True)
tips['time_order'] = np.random.choice(pd.date_range(start='2023-01-01', end='2023-01-31'), size=len(tips))



time_dinamic_button = st.sidebar.button('Динамика чаевых во времени')

if time_dinamic_button:
    tips.sort_values(by=['time_order'], inplace=True)
    st.write('## Динамика чаевых во времени')
    st.line_chart(data=tips, x='time_order', y='tip', x_label='Дата', y_label='Чаевые')


total_bill_button = st.sidebar.button('Гистограмма полного счёта')

if total_bill_button:
    fig = px.histogram(tips, x='total_bill', nbins=15, title='Гистограмма полного счёта')
    fig.update_layout(
    xaxis_title='Полный счёт',
    yaxis_title='Частота')
    st.plotly_chart(fig)


tip_total_scatter_button = st.sidebar.button('Диаграмма рассеяния чаевые/полный счёт')

if tip_total_scatter_button:
    st.write('## Диаграмма рассеяния чаевые/полный счёт')
    st.scatter_chart(data=tips, x='total_bill', y='tip', x_label='Полный счёт', y_label='Чаевые')


size_tip_total_scatter_button = st.sidebar.button('Диаграмма рассеяния чаевые/полный счёт/размер заказа')

if size_tip_total_scatter_button:
    st.write('## Диаграмма рассеяния чаевые/полный счёт/размер заказа')
    st.scatter_chart(data=tips, x='total_bill', y='tip', size='size', x_label='Полный счёт', y_label='Чаевые')


week_total_bill_button = st.sidebar.button('Зависимость полного счёта от дня недели')

if week_total_bill_button:
    st.write('## Зависимость полного счёта от дня недели')
    st.line_chart(data=tips, x='day', y='total_bill', x_label='День недели', y_label='Полный счёт')


sex_week_tip_button = st.sidebar.button('Диаграмма рассеяния день недели/чаевые/пол')

if sex_week_tip_button:
    st.write('## Диаграмма рассеяния день недели/чаевые/пол')
    st.scatter_chart(data=tips, x='tip', y='day', color='sex', x_label='День недели', y_label='Чаевые')


boxplot_button = st.sidebar.button('Ящик с усами с суммой всех счетов за день, разбитых по времени суток')

if boxplot_button:
    fig = px.box(tips, x='day', y='total_bill',color='time')
    fig.update_layout(xaxis_title='День недели', yaxis_title='Сумма полных счетов', legend_title='Время суток')
    st.plotly_chart(fig)


lunch_dinner_button = st.sidebar.button('Гистограмма чаевых днём и вечером')

if lunch_dinner_button:
    lunch_tips = tips[tips['time'] == 'Lunch']['tip'].copy()
    dinner_tips = tips[tips['time'] == 'Dinner']['tip'].copy()
    fig_lunch = px.histogram(lunch_tips, nbins=10, title='Гистограмма чаевых днём')
    fig_dinner = px.histogram(dinner_tips, nbins=10, title='Гистограмма чаевых вечером')
    fig_lunch.update_layout(xaxis_title='Чаевые', yaxis_title='Частота')
    fig_dinner.update_layout(xaxis_title='Чаевые', yaxis_title='Частота')
    st.plotly_chart(fig_lunch)
    st.plotly_chart(fig_dinner)


sex_smoke_button = st.sidebar.button('Диаграммы рассеяния для мужчин и для женщин, курящих и некурящих размер счёта/чаевые')

if sex_smoke_button:
    male_tips = tips[tips['sex'] == 'Male']
    fig_male = px.scatter(
    male_tips,
    x='total_bill',
    y='tip',
    color='smoker',
    title='Среди мужчин: чаевые/полный счёт',
    labels={
        'total_bill': 'Полный счёт',
        'tip': 'Чаевые',
        'smoker': 'Курящий/некурящий'
        })
    female_tips = tips[tips['sex'] == 'Female']
    fig_female = px.scatter(
    female_tips,
    x='total_bill',
    y='tip',
    color='smoker',
    title='Среди женщин: чаевые/полный счёт',
    labels={
        'total_bill': 'Полный счёт',
        'tip': 'Чаевые',
        'smoker': 'Курящая/некурящая'
        })
    st.plotly_chart(fig_male)
    st.plotly_chart(fig_female)


heat_map_button = st.sidebar.button('Тепловая карта зависимости числовых переменных (полного счёта, чаевых и размера счета)')

if heat_map_button:
    fig = plt.figure(figsize=(5, 5))
    numeric_tips = tips.select_dtypes(include=['number'])
    sns.heatmap(data=numeric_tips.corr(), annot=True)
    plt.title('Тепловая карта зависимости числовых переменных')
    plt.tight_layout()
    st.pyplot(fig)