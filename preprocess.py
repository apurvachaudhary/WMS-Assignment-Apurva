import pandas as pd

def clean_sales_data(file_path, mapping_dict):
    df = pd.read_csv(file_path)
    df.dropna(subset=["SKU", "Quantity"], inplace=True)
    df["SKU"] = df["SKU"].str.strip().str.upper()
    df["MSKU"] = df["SKU"].map(mapping_dict)
    df = df[df["MSKU"].notnull()]
    return df

if __name__ == "__main__":
    mapping = {"GLD": "Golden Apple", "ORG": "Orange"}
    result = clean_sales_data("sales_data.csv", mapping)
    result.to_csv("cleaned_sales.csv", index=False)