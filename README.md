# House Rent Prediction System using Machine Learning

---

## Project Description

This project is a **Machine Learning-based House Rent Prediction System** that predicts the **monthly rental price (₹)** of houses and apartments based on various features such as:

- BHK (number of rooms)
- Size (in square feet)
- City
- Furnishing status
- Tenant preference
- Number of bathrooms

The goal of this project is to build an accurate regression model that helps users and businesses estimate rental prices based on property characteristics.

---

## Project Domain

Housing is one of the most basic human needs. The price of a house or apartment depends on multiple factors such as location, size, number of rooms, and amenities.

However, predicting rental prices manually is difficult due to:
- Multiple influencing factors
- Market variability
- Lack of standard pricing rules

This project uses **Machine Learning** to solve this problem by predicting rent based on historical data.

---

## Business Use Case

This system can be used by:

- Real estate companies  
- Property owners  
-  Rental price consultants  

### Applications:
- Estimate fair rental price  
- Avoid underpricing or overpricing  
- Support business decision-making  

---

##  Problem Statement

1. Which features most influence rental price?  
2. How to preprocess real estate data effectively?  
3. How to build an accurate prediction model?  

---

##  Objectives

- Perform Exploratory Data Analysis (EDA)  
- Handle missing values and outliers  
- Transform categorical data into numerical format  
- Train multiple machine learning models  
- Evaluate and compare model performance  
- Deploy the model using Streamlit  

---

##  Dataset Information

- **Source:** Kaggle - House Rent Prediction Dataset  
- **Format:** CSV  
- **Total Samples:** 4746  
- **Features:** 12  
- **Missing Values:** None  

---

##  Dataset Features

| Feature | Description |
|--------|------------|
| Posted On | Date of listing |
| BHK | Number of bedrooms, hall, kitchen |
| Rent | Target variable (monthly rent ₹) |
| Size | Area in square feet |
| Floor | Floor details |
| Area Type | Carpet / Super / Built Area |
| Area Locality | Location |
| City | City of property |
| Furnishing Status | Furnished / Semi / Unfurnished |
| Tenant Preferred | Preferred tenant type |
| Bathroom | Number of bathrooms |
| Point of Contact | Contact info |

---

##  Data Cleaning

### Removed Features:
- `Posted On`
- `Point of Contact`

Reason:
- These features do not impact rental price prediction.

---

##  Exploratory Data Analysis (EDA)

###  Univariate Analysis
- Most houses:
  - 1–3 BHK
  - 1–3 bathrooms
  - Size < 2000 sqft  

- Rent distribution:
  - Range: ₹1200 – ₹3,500,000  
  - Average: ₹35,000  

---

###  Multivariate Analysis

####  Size vs BHK
- Removed unrealistic entries:
  - Less than 300 sqft per BHK  

####  Price per sqft
- Created feature:
  - `Price_per_sqft = Rent / Size`

- Removed extreme outliers using:
  - Mean ± Standard Deviation  

#### ✔Bathroom vs BHK
- Removed invalid data:
  - Bathroom > BHK + 2  

---

###  Categorical Analysis

- **City** → Strong influence (Mumbai highest rent)  
- **Furnishing** → Furnished homes cost more  
- **Tenant Preference** → Family homes cost more  
- **Area Type** → Less impact  

---

##  Data Preprocessing

###  One Hot Encoding
Converted categorical features into numeric format:
- Area Type  
- City  
- Furnishing Status  
- Tenant Preferred  

---

###  Train-Test Split

- Training Data: 95%  
- Testing Data: 5%  

---

###  Feature Scaling

Used:
StandardScaler

To normalize numerical features:
- BHK  
- Size  
- Bathroom  

---

##  Machine Learning Models

### K-Nearest Neighbors (KNN)
- Based on distance between data points  
- Parameter: `n_neighbors`  

---

### Random Forest Regressor
- Ensemble learning method  
- Uses multiple decision trees  

Parameters:
- `n_estimators`  
- `max_depth`  
- `random_state`  

---

### AdaBoost Regressor
- Boosting technique  
- Combines weak learners  

Parameters:
- `n_estimators`  
- `learning_rate`  

---

## Hyperparameter Tuning

Used:
GridSearchCV

### Best Parameters:

| Model | Best Params |
|------|-------------|
| KNN | n_neighbors = 7 |
| AdaBoost | learning_rate=0.1, n_estimators=100 |
| Random Forest | max_depth=8, n_estimators=25 |

---

## Model Evaluation

### Metrics Used:
- R² Score  
- Mean Squared Error (MSE)  

---

### Results

| Model | Accuracy |
|------|----------|
| KNN | 0.72 |
| AdaBoost | 0.89 |
| Random Forest | **0.93** |

 **Best Model: Random Forest**

---

## Streamlit Web Application

The project includes a Streamlit app where users can:

- Enter property details  
- Predict rent instantly  
- View results in real-time  

---

## How to Run the Project

### 1. Clone Repository
git clone https://github.com/divyum25bce10701/House-Rent-predictor-.git
House-rent-predictor

### 2. Create Virtual Environment
python -m venv venv  
venv\Scripts\activate  

### 3. Install Dependencies
pip install -r requirements.txt  

### 4. Run Streamlit App
streamlit run app.py  

---

## Screenshot
<img width="1826" height="897" alt="{09AE2FD0-285D-430B-AE7D-56D7A2CD6504}" src="https://github.com/user-attachments/assets/9224ca5c-9dcf-416d-94b7-d913ace6df83" />

---

##  Output

 The model predicts:  
**Monthly Rent in INR (₹)**  

---

## Future Improvements

- Add location coordinates (latitude/longitude)  
- Use advanced models (XGBoost, LightGBM)  
- Improve UI/UX  
- Deploy on cloud  
- Increase dataset size  

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Streamlit  

---

##  Author

**Divyum Saini**  
B.Tech cse core 
VIT Bhopal  

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!
