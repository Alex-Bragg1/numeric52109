###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##
# Conditional import for required packages (Requirement 5)

try:
    import numpy as np
except ImportError:
    # Define np as None if import fails so logic can check for it
    np = None
    print("Warning: NumPy is not installed. Statistics functions will not work.")

def _validate_input(data):
    # Private function for Requirement 4
    
    if np is None:
        raise RuntimeError("NumPy package is required but not installed.")

    # Convert list to NumPy array (Requirement 4)
    if isinstance(data, list):
        try:
            data = np.array(data, dtype=float)
        except ValueError:
            raise ValueError("Input list contains non-numeric data.")
    
    # Check if the input is a NumPy array (Requirement 4)
    if not isinstance(data, np.ndarray):
        raise TypeError("Input data must be a list or a NumPy array.")
        
    if data.size == 0:
        raise ValueError("Input data cannot be empty.")
        
    return data

def calculate_stats(data):
    """
    Calculates the mean, median, and standard deviation of the input data.
    Input: data (list or numpy.ndarray)
    Output: Dictionary of results. (Requirement 1)
    """
    data = _validate_input(data)

    mean_val = np.mean(data)
    median_val = np.median(data)
    std_dev = np.std(data)
    
    # Requirement 2
    print("\n--- Basic Statistics Results ---")
    print(f"Input Data Size: {data.size}")
    print(f"Mean (Average): {mean_val:.4f}")
    print(f"Median (Midpoint): {median_val:.4f}")
    print(f"Standard Deviation: {std_dev:.4f}")
    print("--------------------------------")
    
    return {
        'data': data,
        'mean': mean_val,
        'median': median_val,
        'std_dev': std_dev
    }