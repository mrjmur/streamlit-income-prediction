import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Заголовок приложения
st.title("Прогнозирование дохода")
st.write("Это приложение предсказывает, превысит ли ваш средний заработок порог $50k.")

# Загрузка модели
@st.cache_resource
def load_model():
    with open('best_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Описание интерфейса
st.sidebar.header("Введите данные")
age = st.sidebar.slider("Возраст", 18, 100, 30)
workclass = st.sidebar.selectbox("Тип работы", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])
education = st.sidebar.selectbox("Образование", ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"])
education_num = st.sidebar.slider("Число лет обучения", 1, 20, 10)
marital_status = st.sidebar.selectbox("Семейное положение", ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
occupation = st.sidebar.selectbox("Профессия", ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"])
relationship = st.sidebar.selectbox("Отношения", ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"])
race = st.sidebar.selectbox("Раса", ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"])
sex = st.sidebar.selectbox("Пол", ["Female", "Male"])
capital_gain = st.sidebar.number_input("Капитальный доход", 0, 100000, 0)
capital_loss = st.sidebar.number_input("Капитальный убыток", 0, 100000, 0)
hours_per_week = st.sidebar.slider("Часов в неделю", 1, 100, 40)

# Преобразование данных в DataFrame
data = {
    "age": age,
    "workclass": workclass,
    "education": education,
    "education-num": education_num,
    "marital-status": marital_status,
    "occupation": occupation,
    "relationship": relationship,
    "race": race,
    "sex": sex,
    "capital-gain": capital_gain,
    "capital-loss": capital_loss,
    "hours-per-week": hours_per_week
}

df = pd.DataFrame(data, index=[0])

# Предобработка данных
# (Здесь нужно добавить код для кодирования категориальных признаков и масштабирования числовых признаков)

# Предсказание
if st.button("Сделать предсказание"):
    prediction = model.predict(df)
    if prediction[0] == 1:
        st.success("Ваш заработок, вероятно, превысит $50k!")
    else:
        st.error("Ваш заработок, вероятно, не превысит $50k.")