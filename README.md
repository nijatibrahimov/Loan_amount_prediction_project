# Loan Amount Prediction Project

## Overview

This project focuses on predicting loan amounts using machine learning techniques. It includes exploratory data analysis, statistical analysis, feature scaling, model development, and evaluation.

A Random Forest Regressor was trained to predict loan amounts based on the available dataset features. The project also includes a Flask web application connected to a MySQL database to support the application's prediction workflow.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Statsmodels
* Scikit-learn
* Random Forest Regressor
* Flask
* MySQL
* HTML
* CSS
* Jupyter Notebook

## Project Structure

```text
loan_amount_prediction_project/
├── static/
│   └── style.css
├── templates/
│   └── project2.html
├── .env
├── .gitignore
├── loan_data.csv
├── project2.ipynb
├── server.py
└── README.md
```

The `.env` file is used for local configuration and must not be uploaded to GitHub. The `.venv/` and `.vscode/` directories are excluded from version control.

## Exploratory Data Analysis

The dataset was explored to understand its characteristics and prepare it for model development.

Statistical analysis was performed using `statsmodels.api`. Variance Inflation Factor (VIF) was also examined to assess multicollinearity among numerical predictors.

## Model Development

A Random Forest Regressor was developed to predict loan amounts.

The workflow included:

* Data exploration and preprocessing
* Multicollinearity analysis using VIF
* Feature scaling
* Model training
* Model evaluation using MAE and R²

## Model Performance

The model achieved the following reported evaluation results:

| Metric                    | Result |
| ------------------------- | -----: |
| Mean Absolute Error (MAE) | 271.42 |
| R² Score                  |  0.995 |

The MAE indicates an average absolute prediction error of approximately 271.42 units of the target variable, while the R² score indicates that the model explains approximately 99.5% of the variance in the evaluation data.

These results should be interpreted in the context of the dataset, the target variable's units, and the evaluation methodology.

## Web Application

The project includes a Flask application connected to a MySQL database.

* `server.py` handles the application logic.
* `project2.html` provides the HTML interface.
* `static/style.css` defines the interface styling.
* MySQL is used for database integration.
* The trained model is used in the application's prediction workflow.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd loan_amount_prediction_project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

Install the dependencies used by the notebook and Flask application.

A `requirements.txt` file should be created to document the project's dependencies.

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file and configure the required MySQL connection settings.

Do not commit database credentials or other secrets to GitHub.

### 5. Configure MySQL

Create the required database and table, and ensure that the database configuration matches the values in your local `.env` file.

### 6. Run the application

```bash
python server.py
```

Follow the local address displayed by Flask to access the web application.

## Future Improvements

* Add additional regression models for comparison.
* Improve feature selection and hyperparameter tuning.
* Add prediction visualizations.
* Improve input validation and error handling.
* Document the database schema and application setup.

## Disclaimer

The reported evaluation metrics describe the model's performance on the evaluation data used during development. They do not guarantee the same performance on unseen real-world data.
