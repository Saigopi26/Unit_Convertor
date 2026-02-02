import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title(" Unit Converter Web App")
# -----------------------------
# Conversion logic
# -----------------------------
def convert_length(value, from_unit, to_unit):
    units = {
        "Millimeter": 0.001,
        "Centimeter": 0.01,
        "Meter": 1,
        "Kilometer": 1000,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34
    }
    return value * units[from_unit] / units[to_unit]


def convert_weight(value, from_unit, to_unit):
    units = {
        "Milligram": 0.001,
        "Gram": 1,
        "Kilogram": 1000,
        "Ounce": 28.3495,
        "Pound": 453.592
    }
    return value * units[from_unit] / units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        value = value + 273.15
    elif from_unit == "Fahrenheit":
        value = (value - 32) * 5/9 + 273.15

    if to_unit == "Celsius":
        return value - 273.15
    elif to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value


# -----------------------------
# UI Section
# -----------------------------
category = st.selectbox(
    "Select Measurement Type",
    ["Length", "Weight", "Temperature"]
)

value = st.number_input("Enter value to convert", value=0.0)

if category == "Length":
    units = ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Mile"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_length(value, from_unit, to_unit)

elif category == "Weight":
    units = ["Milligram", "Gram", "Kilogram", "Ounce", "Pound"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_weight(value, from_unit, to_unit)

else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_temperature(value, from_unit, to_unit)

# -----------------------------
# Output
# -----------------------------
st.success(f"Converted Value: {result:.4f} {to_unit}")
