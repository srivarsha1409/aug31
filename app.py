import streamlit as st
import pandas as pd
import pickle


model = pickle.load(open("mushroom_model.pkl", "rb"))
encoders = pickle.load(open("label_encoders.pkl", "rb"))

feature_encoders = encoders["features"]
target_encoder = encoders["target"]
columns = encoders["columns"]

st.title("🍄 Mushroom Edibility Prediction")
st.write("Predict whether a mushroom is **Edible (e)** or **Poisonous (p)**")

user_input = {}
for col in columns:
    options = feature_encoders[col].classes_  
    user_input[col] = st.selectbox(f"{col}", options)


input_df = pd.DataFrame([user_input])

for col in columns:
    le = feature_encoders[col]
    input_df[col] = le.transform(input_df[col])


if st.button("Predict"):
    pred = model.predict(input_df)[0]
    result = target_encoder.inverse_transform([pred])[0]  

    if result == "e":
        st.success("✅ The mushroom is **Edible**")
    else:
        st.error("⚠️ The mushroom is **Poisonous**")
