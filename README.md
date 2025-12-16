# 💰 Credit Scoring: Loan Payback Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Scikit--Learn%20|%20Pandas%20|%20Seaborn%20|Matplotlib-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📌 Project Overview
This project aims to build a **Credit Scoring Model** to predict the likelihood of a borrower paying back a loan (`loan_paid_back`: 1 for Paid, 0 for Not Paid). 

In the financial industry, accurately assessing credit risk helps lenders minimize default rates and optimize interest rate strategies. This project covers the End-to-End Data Science lifecycle, from EDA and Statistical Testing to Feature Engineering and Modeling.

## 📂 Dataset Overview
* **Training Set:** 593,994 rows, 13 columns.
* **Testing Set:** 254,569 rows.
* **Target Variable:** `loan_paid_back` (Binary Classification).
* **Key Features:** `annual_income`, `credit_score`, `debt_to_income_ratio`, `loan_amount`, `interest_rate`, etc.

## ⚙️ Technical Approach

### 1. Exploratory Data Analysis (EDA) & Cleaning
* **Outlier Detection:** Used **IQR Method** to identify outliers in `annual_income` and `debt_to_income_ratio`. Applied Log Transformation to handle right-skewed distributions.
* **Imbalance Handling:** Analyzed the class distribution (Paid vs. Not Paid) to understand the baseline accuracy.
* **Visualizations:** Boxplots, Histograms, and Correlation Heatmaps to understand feature relationships.

### 2. Feature Selection (Statistical Hypothesis Testing)
Instead of relying solely on intuition, I used statistical tests to select the most relevant features ($P\text{-value} < 0.05$):
* **Numerical Features:** Applied **Mann-Whitney U Test** (due to non-normal distributions).
* **Categorical Features:** Applied **Chi-Square Test**.

### 3. Feature Engineering (Financial Domain Knowledge)
Created new interaction features to capture the borrower's **Cash Flow** and **Leverage**:
* `loan_to_income`: Ratio of loan amount to annual income.
* `monthly_disposable_income`: Estimated remaining monthly cash flow after existing debts.
* `income_rank`: Binned annual income into Low/Medium/High groups to handle outliers.
* `score_efficiency`: Ratio of Credit Score to Interest Rate.

### 4. Data Preprocessing
* **Skewness Handling:** Applied `np.log1p` for highly skewed features (`annual_income`, `loan_amount`).
* **Scaling:** Used `StandardScaler` to normalize numerical features for Logistic Regression.
* **Encoding:** One-Hot Encoding for categorical variables.

### 5. Modeling
* **Algorithm:** Logistic Regression (with `lbfgs` solver and tuned `max_iter` for convergence), Random Forest and XGBoost (with `10` max depth and `0.01` learning rate).

## 📊 Results & Evaluation

| Model | Accuracy | Precision | Recall |
| :----- | :--------: | :---------: | ------: |
| **Logistic Regression** | 88.94 | 81.12 | 58.62 |
| **Random Forest** | 99.99 | 87.37 | 59.51 |
| **XGBoost** | 90.16 | 95.55 | 52.45 |

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/credit-scoring-project.git](https://github.com/your-username/credit-scoring-project.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the notebook:**
    Open `main.ipynb` (or your notebook name) to view the analysis and training process.

## 🔮 Future Improvements
* Implement SMOTE or Class Weighting to better handle the class imbalance.
* Deploy the model as a simple API using Flask or FastAPI.

---
**Author:** Nguyen Manh Hung<br>