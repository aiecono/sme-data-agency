import pandas as pd

def clean_data(df):
    # Remove cancellations and returns
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    
    # Remove negative and zero quantity
    df = df[df['Quantity'] > 0]
    
    # Remove negative and zero unit price
    df = df[df['UnitPrice'] > 0]
    
    # Remove missing CustomerID
    df = df.dropna(subset=['CustomerID'])
    
    # Remove missing Description
    df = df.dropna(subset=['Description'])
    
    return df


def validate_data(df):
    assert df['Quantity'].min() > 0, "Error: negative quantities found"
    assert df['UnitPrice'].min() > 0, "Error: zero or negative prices found"
    assert df['CustomerID'].isnull().sum() == 0, "Error: missing CustomerIDs found"
    assert df['Description'].isnull().sum() == 0, "Error: missing Descriptions found"
    print("All checks passed. Data is clean.")