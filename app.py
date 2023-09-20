# app.py
!pip install pypmml
!pip install streamlit
import streamlit as st
from pypmml import Model


# Ensure you have the correct path to your PMML file here
pmml_file_path = 'test3.0.pmml'

# Load PMML Model
model = Model.fromFile(pmml_file_path)

# Create a function to predict selling price
def predict_price(car_model, age, mileage):
    # Map car model to respective input format
    bmw_x5 = 1 if car_model == "BMW X5" else 0
    audi_a5 = 1 if car_model == "Audi A5" else 0
    mercedes_benz_c = 1 if car_model == "Mercedes Benz C class" else 0
    # Construct input data based on the format expected by your model
    input_data = {
        "BMW X5": bmw_x5,
        "Audi A5": audi_a5,
        "Age": age,
        "Mileage": mileage
    }

    # Use the model to predict
    result = model.predicy(input_data)   
    return result[0]
      # assuming it returns a list, get the first item which is the predicted price.

# Streamlit App UI
st.title("Car Selling Price Predictor")

# Dropdown for car model selection
car_model = st.selectbox("Select Car Model", ["BMW X5", "Audi A5", "Mercedes Benz C class"])

# Input boxes for Age and Mileage
age = st.number_input("Enter Age of the Car", min_value=0, max_value=100, step=1)
mileage = st.number_input("Enter Mileage of the Car", min_value=0, max_value=1000000, step=100)

# Predict button
if st.button("Predict Selling Price"):
    price = predict_price(car_model, age, mileage)
    st.write(f"The estimated selling price is: ${price}")
