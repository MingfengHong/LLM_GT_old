# project_directory/data/data_processing.py

import pandas as pd

def read_excel_file(file_path):
    """
    读取 Excel 文件并返回 DataFrame。
    """
    try:
        df = pd.read_excel(file_path)
        print(f"Successfully read the file: {file_path}")
        return df
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def write_excel_file(df, file_path):
    """
    将 DataFrame 写入 Excel 文件。
    """
    try:
        df.to_excel(file_path, index=False)
        print(f"Successfully saved the file: {file_path}")
    except Exception as e:
        print(f"Error saving file {file_path}: {e}")

def clean_data(df):
    """
    对 DataFrame 进行一些常见的数据清理操作，例如处理缺失值。
    """
    # 去除所有列中的缺失值（可以根据需求调整）
    df_cleaned = df.dropna()
    print("Data cleaned successfully.")
    return df_cleaned

def add_missing_columns(df, expected_columns):
    """
    确保 DataFrame 包含预期的列。如果缺少列，添加空值列。
    """
    for col in expected_columns:
        if col not in df.columns:
            df[col] = None
    return df

def merge_dataframes(df1, df2, on_columns):
    """
    合并两个 DataFrame，依据给定的列进行合并。
    """
    merged_df = pd.merge(df1, df2, on=on_columns, how='outer')
    print("DataFrames merged successfully.")
    return merged_df
