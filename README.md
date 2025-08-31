# 🍄 Mushroom Edibility Prediction  

This project predicts whether a mushroom is **edible** or **poisonous** based on its characteristics using **machine learning models**.  
It includes data preprocessing, model training (Logistic Regression, Random Forest, Gradient Boosting), model evaluation, hyperparameter tuning, and deployment with **Streamlit**.  

🔗 **Live App:** https://eh65shrzifknm2m4upaycc.streamlit.app/  

---

## 🚀 Overview  

- Preprocessed mushroom dataset (categorical features encoded using `LabelEncoder`)  
- Trained multiple models (Logistic Regression, Random Forest, Gradient Boosting)  
- Evaluated with **accuracy, precision, recall, F1-score, confusion matrix, cross-validation**  
- Tuned Gradient Boosting model for best performance  
- Built a **Streamlit web app** for real-time predictions  
- Visualized data distribution and class balance  

---

## 📂 Project Structure  

```

Mushroom-edibility/
│-- mushroom.ipynb          # Jupyter notebook with preprocessing, training & evaluation
│-- app.py                  # Streamlit app for predictions
│-- mushroom\_model.pkl      # Saved trained model
│-- label\_encoders.pkl      # Encoders for categorical features
│-- requirements.txt        # Required dependencies
│-- README.md               # Project documentation
│-- data/                   # Dataset (if included)

````

---

## 🛠️ Installation  

1. Clone the repository:  
```bash
git clone https://github.com/your-username/mushroom-edibility.git
cd mushroom-edibility
````

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Add these in your **requirements.txt**:

```
numpy
pandas
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

---

## ▶️ Usage

### Run Jupyter Notebook

To retrain or experiment with models:

```bash
jupyter notebook mushroom.ipynb
```

### Run Streamlit App

For live prediction UI:

```bash
streamlit run app.py
```

---

## 📊 Visualizations

* Class distribution (edible vs poisonous)
* Feature importance (for tree-based models)
* Confusion matrices for all models

---

## 🌐 Deployment

The app is deployed to **Streamlit Cloud** 
# 🍄 Mushroom Edibility Prediction  

This project predicts whether a mushroom is **edible** or **poisonous** based on its characteristics using **machine learning models**.  
It includes data preprocessing, model training (Logistic Regression, Random Forest, Gradient Boosting), model evaluation, hyperparameter tuning, and deployment with **Streamlit**.  

🔗 **Live App:**https://eh65shrzifknm2m4upaycc.streamlit.app/

##PREVIEW:
---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9736a2e6-d756-40c6-a2b0-ff209b5d4243" />



## ✨ Future Improvements

* Try more advanced models (XGBoost, LightGBM, Neural Networks)
* Add SHAP/Explainable AI for feature importance
* Improve UI/UX of the Streamlit app

---

## 👩‍💻 Author

Developed by **Sri Varsha** 🚀




