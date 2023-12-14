<h1 align="center">Welcome to Loan Approval Predictor 👋</h1>
<p>
  <a href="https://github.com/Rishitabansal9/Loan-Approval-Predictor/blob/main/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

> This project focuses on predicting loan approvals using machine learning techniques. It encompasses an end-to-end machine learning pipeline, exploratory data analysis (EDA) notebooks, and code for model deployment on the Render platform.

## Dataset

This  data set has 207 rows and 15 columns. 
Key Features:
- Demographics: Age, Gender, State, and City provide a snapshot of the applicant's background.
- Financial Information: Income, Credit Score, and Credit History Length offer insights into the applicant's financial stability and credit behavior.
- Loan Details: The dataset sheds light on the specifics of the loan the applicant is seeking, with details like Loan Amount, Loan Tenure, and Loan to Value (LTV) Ratio.
- Employment Information: The dataset includes both a general employment profile (e.g., Salaried, Self-Employed) and a specific occupation, giving a nuanced view of the applicant's employment status.
- Profile Score: A composite score, ranging from 0 to 100, represents the overall credit profile of the applicant. This score can serve as a quick reference for gauging the creditworthiness of an individual. 

## Structure
```
Loan-Approval_Predictor/
│
├── artifacts/
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
│
├── notebook/
│   ├── data/
│   │   └── credit_data.csv
│   └── Loan_approval.ipynb
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
|
├── static/
│   └── style.css
|
├── templates/
│   └── index.html
|
├── .gitignore
|
├── README.md
|
├── app.py
|
├── requirements.txt
|
└── setup.py
```




### 🏠 [Homepage](https://github.com/Rishitabansal9/Loan-Approval-Predictor/blob/main/README.md)

### ✨ [Demo](https://loan-approval-predictor-es8r.onrender.com/)

## Install

```sh
npm install
```

## Usage

```sh
1. Clone the repository:
   git clone https://github.com/YourUsername/Loan-Approval-Predictor.git
   cd Loan-Approval-Predictor
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
  python app.py
```

## Author

👤 **Rishita Bansal**

* Github: [@Rishitabansal9](https://github.com/Rishitabansal9)
* LinkedIn: [@rishita-bansal-589056143](https://linkedin.com/in/rishita-bansal-589056143)

## Show your support

Give a ⭐️ if this project helped you!
