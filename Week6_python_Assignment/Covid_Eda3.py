# covid_eda.py
# -----------------------------------------------------------
# COVID EDA Program
# Performs:
# 1. Data loading
# 2. Descriptive statistics
# 3. Outlier detection & removal (IQR)
# 4. Normalization using StandardScaler
# 5. Visualization (histograms & heatmap)
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class CovidEDA:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cleaned_df = None
        self.scaled_df = None

    #  Load dataset and keep only Confirmed and New cases columns
    def load_data(self):
        df = pd.read_csv(self.file_path)
        print("\n Dataset loaded successfully!")
        print(f"Columns in file: {list(df.columns)}")

        # Auto-detect relevant columns
        confirmed_col = [col for col in df.columns if 'confirm' in col.lower()][0]
        new_col = [col for col in df.columns if 'new' in col.lower()][0]

        # Keep only required columns
        self.df = df[[confirmed_col, new_col]].copy()
        self.df.columns = ['Confirmed', 'New cases']

        print(f"\n Columns used for analysis: {self.df.columns.tolist()}")
        print(f"Total rows: {len(self.df)}")
        return self.df

    #  Compute statistical measures
    def compute_statistics(self):
        print("\n=====  Descriptive Statistics =====")
        print("Mean:\n", self.df.mean())
        print("\nMedian:\n", self.df.median())
        print("\nVariance:\n", self.df.var())
        print("\nStandard Deviation:\n", self.df.std())
        print("\nCorrelation Matrix:\n", self.df.corr())

    #  Outlier detection using IQR
    def detect_and_remove_outliers(self):
        print("\n=====  Outlier Detection (IQR) =====")
        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        print("\nBounds:")
        print(pd.DataFrame({'Lower': lower_bound, 'Upper': upper_bound}))

        condition = ~(
            (self.df < lower_bound) | (self.df > upper_bound)
        ).any(axis=1)

        self.cleaned_df = self.df[condition].reset_index(drop=True)

        print(f"\nRemoved {len(self.df) - len(self.cleaned_df)} outliers.")
        print(f"Remaining rows: {len(self.cleaned_df)}")
        return self.cleaned_df

    #  Normalize data using StandardScaler
    def normalize_data(self):
        print("\n=====  Normalization using StandardScaler =====")
        scaler = StandardScaler()
        scaled = scaler.fit_transform(self.cleaned_df[['Confirmed', 'New cases']])

        self.scaled_df = pd.DataFrame(
            scaled, columns=['Confirmed_scaled', 'New_cases_scaled']
        )
        print("\nFirst 5 rows of scaled data:")
        print(self.scaled_df.head())
        return self.scaled_df

    #  Visualization
    def visualize(self):
        print("\n=====  Visualization =====")

        # Histograms (before normalization)
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        sns.histplot(self.df['Confirmed'], bins=30, kde=True, color='skyblue')
        plt.title('Confirmed (Before Normalization)')

        plt.subplot(1, 2, 2)
        sns.histplot(self.df['New cases'], bins=30, kde=True, color='orange')
        plt.title('New Cases (Before Normalization)')
        plt.show()

        # Histograms (after normalization)
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        sns.histplot(self.scaled_df['Confirmed_scaled'], bins=30, kde=True, color='green')
        plt.title('Confirmed (After Normalization)')

        plt.subplot(1, 2, 2)
        sns.histplot(self.scaled_df['New_cases_scaled'], bins=30, kde=True, color='purple')
        plt.title('New Cases (After Normalization)')
        plt.show()

        # Correlation Heatmap
        plt.figure(figsize=(5, 4))
        sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm')
        plt.title('Heatmap: Confirmed vs New Cases')
        plt.show()

# -------------- MAIN EXECUTION --------------
if __name__ == "__main__":
    #  Change the path to your dataset location
    file_path = "country_wise_latest.csv"

    eda = CovidEDA(file_path)
    eda.load_data()
    eda.compute_statistics()
    eda.detect_and_remove_outliers()
    eda.normalize_data()
    eda.visualize()
