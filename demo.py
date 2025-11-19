# This is a file to test the statistics, operations and graphics modules in the simple_package

import simple_package.operations as op
import simple_package.statistics as sp_stats
import simple_package.graphics as sp_graphics
import numpy as np

if __name__ == '__main__':
# Testing the calculator app 
    print("\n--- Starting Calculator Test (Type 'exit' to quit) ---")
    op.run_calculator()
    print("--- Calculator Test Finished ---")

### Test cases for statistics.py and graphics.py ### 
    # Sample data
    rng = np.random.default_rng(42)
    test_data = rng.normal(size= 1000)

    try:
        # 1. Calculate stats and display results (Requirement 1 & 2)
        results = sp_stats.calculate_stats(test_data)
        
        # 2. Plot the results (Requirement 3)
        sp_graphics.plot_histogram_with_stats(
            results['data'], 
            results['mean'], 
            results['median']
        )

    except (RuntimeError, TypeError, ValueError) as e:
        print(f"\nFATAL ERROR: Failed to run statistics and graphics: {e}")
    
    
    