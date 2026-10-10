# 🏠 Boston House Price Prediction

A machine learning project that predicts median housing prices in Boston using key socio-economic and structural features. 📊

🔗 **Live demo:** https://house-price-prediction-44.streamlit.app/

<img width="1000" height="705" alt="image" src="https://github.com/user-attachments/assets/9a623d39-43ac-467d-8cf1-8b1b7bc7dca7" />



## 🧠 Technical Summary

- 🤖 **Algorithm:** Multiple Linear Regression (scikit-learn)
- 🏷️ **Features:** Average rooms (`RM`), % lower-status population (`LSTAT`), and pupil-teacher ratio (`PTRATIO`)
- ✂️ **Validation:** 80/20 train-test split
- 📈 **Performance:** R² score of 0.63 on the test set
- 🚀 **Deployment:** Streamlit app hosted on Streamlit Community Cloud

## 📉 Results

The model captures the main trend between predicted and actual prices (R² = 0.63), though predictions are less accurate for very high-priced homes. See the regression plot in the notebook. 🔍

## 📁 Project Files

| File | Description |
|------|-------------|
| 📓 `Boston Housing Price Prediction.ipynb` | Data exploration, training, and evaluation |
| 🖥️ `app.py` | Streamlit web app |
| 📦 `house_model.pkl` | Trained model |
| 🗂️ `housing.data` | Dataset |
| 📋 `requirements.txt` | Python dependencies |

## 💻 Run Locally

```bash
git clone https://github.com/radhikamangal1981-creator/Boston-House-Price-Prediction.git
cd Boston-House-Price-Prediction
pip install -r requirements.txt
streamlit run app.py
```

## ⚠️ Notes on the Dataset

- 🕰️ Prices come from the 1970s, so predictions are for demonstration only, not real market values.
- 🚫 The dataset's `B` column encodes racial composition and is known to be ethically problematic. It was deliberately **not used** as a feature in this model.

## 🔮 Future Improvements

- 🌲 Try Ridge/Lasso regression and tree-based models (Random Forest, XGBoost)
- ⚖️ Add more features and feature scaling
