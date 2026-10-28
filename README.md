# Loan Amount Prediction Project

## Overview

This project aims to predict loan amounts using machine learning techniques. It combines exploratory data analysis, statistical analysis, data preprocessing, model development, and evaluation with a Flask web application integrated with a MySQL database.

A Random Forest Regressor was developed to predict loan amounts based on the available dataset features. The project also includes a Jupyter Notebook documenting the data analysis and model development process.

## Technologies Used

* **Programming Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Statistical Analysis:** Statsmodels
* **Machine Learning:** Scikit-learn, Random Forest Regressor
* **Web Framework:** Flask
* **Database:** MySQL
* **Frontend:** HTML, CSS
* **Development Environment:** Jupyter Notebook

## Project Structure

```text
loan_amount_prediction_project/
├── static/
│   └── style.css
├── templates/
│   └── project2.html
├── .gitignore
├── loan_data.csv
├── project2.ipynb
├── requirements.txt
├── server.py
└── README.md
```

**Note:** The `.env` file contains local environment variables and must not be committed to GitHub. The `.venv/` and `.vscode/` directories are excluded from version control.

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the dataset, examine feature distributions, and prepare the data for machine learning.

The analysis included:

* Exploring dataset characteristics and feature relationships.
* Performing statistical analysis using `statsmodels.api`.
* Examining multicollinearity using the Variance Inflation Factor (VIF).
* Preparing the data for model training.

## Model Development

A Random Forest Regressor was used to predict loan amounts.

The model development workflow included:

1. Data exploration and preprocessing.
2. Multicollinearity analysis using VIF.
3. Feature scaling.
4. Model training.
5. Model evaluation using Mean Absolute Error (MAE) and R².

The model development process and analysis are documented in `project2.ipynb`.

## Model Performance

The model achieved the following evaluation results:

| Evaluation Metric         | Result |
| ------------------------- | -----: |
| Mean Absolute Error (MAE) | 271.42 |
| R² Score                  |  0.995 |

### Interpretation

* **MAE = 271.42:** The model's predictions differ from the actual loan amounts by an average absolute error of approximately 271.42 units of the target variable.
* **R² = 0.995:** The model explains approximately 99.5% of the variance in the target variable on the evaluated dataset.

These results indicate strong performance on the evaluation data. However, further validation on unseen data is important to assess the model's generalization capability.

## Web Application

The project includes a Flask web application integrated with a MySQL database.

The main components are:

* **`server.py`:** Handles the Flask application logic and database integration.
* **`templates/project2.html`:** Provides the web interface.
* **`static/style.css`:** Defines the interface styling.
* **MySQL:** Supports database operations.
* **Machine Learning Model:** Provides loan amount predictions within the application workflow.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nijatibrahimov/Loan_amount_prediction_project.git
cd Loan_amount_prediction_project
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a local `.env` file in the project root directory.

Add the environment variables required by `server.py` for the MySQL connection. Use the variable names expected by the application.

**Do not upload your `.env` file or expose database credentials in your repository.**

### 5. Configure MySQL

Ensure that MySQL is installed and running.

Create the database and required table expected by the application. Verify that the database name, table structure, and connection settings match the configuration used in `server.py`.

### 6. Run the Application

```bash
python server.py
```

Open the local address displayed in the terminal to access the web application.

## Future Improvements

* Compare Random Forest with other regression algorithms.
* Perform hyperparameter tuning.
* Improve feature selection and preprocessing.
* Add prediction visualizations.
* Improve input validation and error handling.
* Document the database schema and configuration.
* Evaluate model performance on additional unseen data.

## Disclaimer

The reported metrics reflect the model's evaluation results on the dataset used during development. They do not guarantee equivalent performance on unseen data or in real-world lending scenarios.
