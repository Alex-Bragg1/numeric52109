# Conditional imports (Requirement 5)
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print("Warning: Matplotlib is not installed. Plotting functions will not work.")

# Import the statistics module to use its functions (e.g., _validate_input)
# Assuming 'simple_package' is the parent folder
# from . import statistics # This relative import works best inside the package structure

# Since we can't easily do a relative import here without running it inside the package, 
# for testing simplicity, we'll assume the statistics functions are available or passed in.

def plot_histogram_with_stats(data, mean_val, median_val):
    """
    Plots a histogram of the data with lines marking the mean and median. (Requirement 3)
    """
    if plt is None:
        raise RuntimeError("Matplotlib package is required for plotting but not installed.")
    
    if not hasattr(data, 'size'):
        # Simple check in case data wasn't a numpy array 
        raise TypeError("Plotting function requires NumPy array data.")

    plt.figure(figsize=(10, 6))
    
    # Plot the histogram
    plt.hist(data, bins='auto', edgecolor='black', alpha=0.7, label='Data Distribution')
    
    # Mark Mean and Median (Requirement 3)
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean ({mean_val:.2f})')
    plt.axvline(median_val, color='green', linestyle='solid', linewidth=2, label=f'Median ({median_val:.2f})')
    
    # Add labels and title
    plt.title('Histogram of Data with Mean and Median')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.show()