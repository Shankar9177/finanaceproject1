# transformations in this file

# transformations.py
 # This module contains various data transformation functions
def normalize_data(data):
    """Normalize the input data to a range of [0, 2]."""
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]  
