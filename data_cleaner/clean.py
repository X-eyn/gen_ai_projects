import pandas as pd
import numpy as np
from scipy.stats import zscore


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def handle_missing_values(df):
    initial_shape = df.shape
    print(
        f"Initial data shape: {initial_shape[0]} rows, {initial_shape[1]} columns")

    missing_cols = df.columns[df.isnull().any()]
    print(f"Columns with missing values: {missing_cols.tolist()}")

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    final_shape = df.shape
    print(
        f"After handling missing values: {final_shape[0]} rows, {final_shape[1]} columns")

    return df


def handle_outliers(df):

    initial_shape = df.shape
    print(
        f"Initial data shape before outlier removal: {initial_shape[0]} rows, {initial_shape[1]} columns")

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    print(f"Numerical columns: {numerical_cols.tolist()}")

    z_scores = np.abs(zscore(df[numerical_cols].dropna()))
    rows_before = df.shape[0]

    df_no_outliers = df[(z_scores < 3).all(axis=1)]
    rows_after = df_no_outliers.shape[0]
    print(
        f"Removed {rows_before - rows_after} rows due to outliers (Z-score > 3)")

    final_shape = df_no_outliers.shape
    print(
        f"After outlier removal: {final_shape[0]} rows, {final_shape[1]} columns")

    return df_no_outliers


def remove_duplicates(df):

    initial_shape = df.shape
    print(
        f"Initial data shape before duplicate removal: {initial_shape[0]} rows, {initial_shape[1]} columns")

    before_dedup = df.shape[0]
    df_no_duplicates = df.drop_duplicates()
    after_dedup = df_no_duplicates.shape[0]
    print(f"Removed {before_dedup - after_dedup} duplicate rows")

    final_shape = df_no_duplicates.shape
    print(
        f"After duplicate removal: {final_shape[0]} rows, {final_shape[1]} columns")

    return df_no_duplicates


def clean_dataset(file_path):
    df = load_data(file_path)
    df_cleaned = handle_missing_values(df)
    df_cleaned = handle_outliers(df_cleaned)
    df_cleaned = remove_duplicates(df_cleaned)
    return df_cleaned


file_path = 'C:/Users/Admin/Downloads/titanic/train.csv'
df_cleaned = clean_dataset(file_path)


df_cleaned.to_csv('cleaned_train.csv', index=False)
print(f"Cleaned dataset saved to 'cleaned_train.csv'")
