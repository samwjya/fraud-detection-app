import streamlit as st
import requests

st.title("💳 Fraud Detection Dashboard")
st.markdown("Upload a CSV file containing transaction data to check for fraud.")

uploaded_file = st.file_uploader("Uplaod a CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄Preview:")
    st.dataframe(df.head())

    expected_features = [f"V{i}" for i in range(1,29)] + ["Amount"]
    input_row = df.iloc[0]

    model_input = {feature: 0.0 for feature in expected_features}

    for col in df.columns:
        if col in model_input:
            model_input[col] = float(input_row[col])

    st.write("Formatted input for model: ")
    st.json(model_input)

    if st.button("Predict"):
        try:
            response = response.post("http://127.0.0.1:8000/predict", json=model_input)
            result = response.json()

            if result.get("fraud") == True:
                st.error("🚨 Fraudulent Transaction Detected!")
            else:
                st.success("✅ This transaction is safe.")
        
        except Exception as e:
            st.error(f"Error: {str(e)}")


