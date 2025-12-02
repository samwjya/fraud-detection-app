# Fraud Detection Project
- A data visualization dashboard that analyzes financial transactions and predicts potential fraud using a machine learning model.
- Built with Streamlit (frontend/UI) and FastAPI (backend API)
- Deployed on Streamlit (Frontend) and Render (Backend)


# Features
- Interactive dashboard UI built with Streamlit
- CSV upload to analyze custom transaction datasets
- Random Forest fraud detection model
- Visual summary of predictions, including:
- Class distribution pie chart
- Total, safe, and fraudulent transaction counts
- Downloadable prediction results (CSV)

# Demo
![Before upload Section](/demo/demo1.png)
![After upload Section](/demo/demo2.png)
![Summary Section](/demo/demo3.png)

# Steps to Run Locally
### 1. Clone this repo
```bash
git clone https://github.com/samwjya/fraud-detection-app.git
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Start the backend
```bash
uvicorn app:app --reload
```
5. Run the Streamlit dashboard
```bash
streamlit run streamlit_app.py
```

