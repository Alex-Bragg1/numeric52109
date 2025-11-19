###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package.operations as op

if __name__ == '__main__':
    ## Define two numbers
    a = 1
    b = 2
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {op.multiply(a,b)}")   
    
    
    # Testing the calculator app 
    print("\n--- Starting Calculator Test (Type 'exit' to quit) ---")
    op.run_calculator()
    print("--- Calculator Test Finished ---")

    ### Test cases for statistics.py and graphics.py ### 
    import simple_package.statistics as sp_stats
    import simple_package.graphics as sp_graphics
    import numpy as np

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
    
    
    
    
    