import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing values in each column:")
    print(df.isnull().sum())
except Exception as e:
    print("Error loading dataset:", e)
    exit()

# Task 2: Basic Data Analysis
print("\nDescriptive Statistics:")
print(df.describe())

print("\nMean measurements per species:")
group_means = df.groupby('species').mean()
print(group_means)

# Task 3: Data Visualization
sns.set(style="whitegrid")

# 1. Line Chart (simulated time-series just for illustration)
df_time = df.copy()
df_time['Index'] = df_time.index
plt.figure(figsize=(8, 5))
sns.lineplot(data=df_time, x='Index', y='sepal length (cm)', hue='species')
plt.title('Sepal Length Over Index (Simulated Time)')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.savefig("line_chart_sepal_length.png")
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
group_means['petal length (cm)'].plot(kind='bar', color=['skyblue', 'salmon', 'limegreen'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.savefig("bar_chart_petal_length.png")
plt.show()

# 3. Histogram
plt.figure(figsize=(6, 4))
plt.hist(df['petal length (cm)'], bins=20, edgecolor='black', color='orchid')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("histogram_petal_length.png")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set2')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.savefig("scatter_sepal_vs_petal.png")
plt.show()

# Findings
print("\nFindings:")
print("- Setosa has the shortest petal length on average.")
print("- Virginica has the largest petal and sepal sizes.")
print("- Clear linear relationship between sepal and petal length for most species.")
