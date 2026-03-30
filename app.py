import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("rent_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))


def predict_rent(BHK, Size, Bathroom, area_type, city, furnishing, tenant):
    x = np.zeros(len(columns))

    x[columns.index('BHK')] = BHK
    x[columns.index('Size')] = Size
    x[columns.index('Bathroom')] = Bathroom

    x[columns.index(f'Area Type_{area_type}')] = 1
    x[columns.index(f'City_{city}')] = 1
    x[columns.index(f'Furnishing Status_{furnishing}')] = 1
    x[columns.index(f'Tenant Preferred_{tenant}')] = 1

    num_idx = [
        columns.index('BHK'),
        columns.index('Size'),
        columns.index('Bathroom')
    ]

    x[num_idx] = scaler.transform([x[num_idx]])[0]

    return model.predict([x])[0]

st.set_page_config(page_title="House Rent Predictor", page_icon="🏠", layout="wide")

st.markdown("<h1 style='text-align: center;'>🏠 AI House Rent Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Smart ML-based rent estimation</p>", unsafe_allow_html=True)

st.divider()


col1, col2 = st.columns(2)

with col1:
    st.subheader("Property Details")

    bhk = st.slider("BHK", 1, 10, 2)
    size = st.slider("Size (sqft)", 100, 5000, 1000)
    bathroom = st.slider("Bathrooms", 1, 10, 2)

with col2:
    st.subheader("Additional Info")

    area_type = st.selectbox("Area Type", ["Carpet Area", "Super Area"])
    city = st.selectbox("City", ["Bangalore", "Mumbai", "Delhi", "Chennai", "Kolkata", "Hyderabad"])
    furnishing = st.selectbox("Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])
    tenant = st.selectbox("Tenant Preferred", ["Bachelors", "Family", "Bachelors/Family"])

st.divider()

col_center = st.columns([1,2,1])[1]

with col_center:
    predict_btn = st.button("Predict Rent", use_container_width=True)

if predict_btn:
    rent = predict_rent(bhk, size, bathroom, area_type, city, furnishing, tenant)

    st.success(f"Estimated Monthly Rent: ₹ {round(rent, 2)}")

  
st.info("💡 Rent shown is per month (INR)")
