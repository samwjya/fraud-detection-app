import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Fraud Detection Dashboard", page_icon="💳", layout = "centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💳 Fraud Detection Dashboard</h1>", unsafe_allow_html=True)
st.write("Upload a CSV file below to detect whether a transaction is fraudulent or not.")
st.markdown("---")

with st.sidebar:
    st.markdown("### 📁 Project Info")
    st.markdown("- Built with Streamlit + FastAPI")
    st.markdown("- Random Forest model")
    st.markdown("---")
    st.markdown("👤 Created by: Samuel Wijaya")


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

    if st.button("Analyze All Transactions"):
        try:
            fraud_count = 0
            not_fraud_count = 0
            total = df.shape[0]
            predictions = []
            
            for index, row in df.iterrows():
                model_input = {feature: 0.0 for feature in expected_features}

                for col in df.columns:
                    if col in model_input:
                        model_input[col] = float(row[col])
               
                response = requests.post("https://fraud-detection-app-8tze.onrender.com/predict", json=model_input)
                result = response.json()

                is_fraud = result.get("fraud", False)
                predictions.append("Fraud! " if is_fraud else "Safe ")

                if is_fraud:
                    fraud_count += 1
                else:
                    not_fraud_count += 1

            st.success(f"✅ Total Transactions: {total}")
            st.error(f"🚨 Predicted Fraudulent Transactions: {fraud_count}")
            st.info(f"✅ Predicted Safe Transactions: {not_fraud_count}")

            st.markdown("### Class Distribution")
            labels = ["Not Fraud", "Fraud"]
            values = [not_fraud_count, fraud_count]
            colors=["#66bb6a", "#ef5350"]
            fig, ax = plt.subplots()

            ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors )
            ax.axis("equal")
            st.markdown("### 🧮 Prediction Summary")
            st.pyplot(fig)

            df["predictions"] = predictions

            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index = False)
            csv_data = csv_buffer.getvalue().encode("utf-8")

            st.download_button(
                label="Download results as CSV",
                data=csv_data,
                file_name="predicted_results.csv",
                mime="text/csv"
            )
        
        except Exception as e:
            st.error(f"Error: {str(e)}")


