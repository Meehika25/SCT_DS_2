🚢 Titanic Dataset - Data Cleaning & Exploratory Data Analysis (EDA)
📌 Overview

This project demonstrates data cleaning and exploratory data analysis (EDA) on the Titanic dataset.
The goal is to explore relationships between variables, handle missing values, and identify patterns and trends in survival outcomes.

The dataset contains information about passengers such as their age, class, gender, fare, and survival status.

📂 Dataset

The dataset used is a sample Titanic dataset (titanic.csv).
It includes the following columns:

PassengerId – Unique identifier for each passenger

Survived – Survival indicator (0 = Did not survive, 1 = Survived)

Pclass – Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)

Name – Passenger name

Sex – Gender of the passenger

Age – Passenger age

SibSp – Number of siblings/spouses aboard

Parch – Number of parents/children aboard

Ticket – Ticket number

Fare – Fare paid by the passenger

Cabin – Cabin number (may contain missing values)

Embarked – Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

⚙️ Installation & Setup

Clone or download this repository.

Install required dependencies:

pip install pandas matplotlib seaborn


Place the dataset file titanic.csv in the same folder as your script.

▶️ Usage

Run the Python script:

python task2.py


This will:

Display the first few rows of the dataset

Show dataset information (columns, datatypes, missing values)

Perform cleaning and exploratory analysis

Generate visualizations (if included)

🔎 Key Steps in EDA

Data Cleaning

Handling missing values in Age, Cabin, Embarked.

Converting categorical variables (Sex, Embarked) into usable format.

Exploratory Analysis

Distribution of passengers by class, gender, and age.

Relationship between survival and gender/class.

Correlation of fare and survival.

Visualizations (Optional)

Bar plots, histograms, heatmaps to identify trends.
