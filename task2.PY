# Titanic EDA Example
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (change path if needed, or use Kaggle link)
df = pd.read_csv("titanic.csv")

# -------------------
# 1. Basic Info
# -------------------
print("First 5 rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# -------------------
# 2. Data Cleaning
# -------------------
# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

print("\nAfter Cleaning:")
print(df.isnull().sum())

# -------------------
# 3. Exploratory Data Analysis (EDA)
# -------------------

# Survival count
sns.countplot(data=df, x='Survived')
plt.title("Survival Count")
plt.show()

# Survival by Gender
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title("Survival by Gender")
plt.show()

# Survival by Passenger Class
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title("Survival by Passenger Class")
plt.show()

# Age distribution by Survival
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True)
plt.title("Age Distribution by Survival")
plt.show()

# -------------------
# 4. Correlation Heatmap
# -------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
