import pandas as pd
import numpy as np

def calculate_store_age_func(X):
    return (2026 - X).values

def extract_product_id_char_func(X):
    return X.iloc[:, 0].astype(str).apply(lambda s: s[:2]).values.reshape(-1, 1)

def standardize_sugar_content(X):
    return X.iloc[:, 0].astype(str).replace('reg', 'Regular').values.reshape(-1, 1)

def classify_product_type_category(X):
    perishable_types = [
        'Fruits and Vegetables', 'Dairy', 'Meat', 'Breads',
        'Seafood', 'Breakfast', 'Starchy Foods', 'Frozen Foods'
    ]
    return X.iloc[:, 0].astype(str).apply(lambda x: 'Perishables' if x in perishable_types else 'Non Perishables').values.reshape(-1, 1)
