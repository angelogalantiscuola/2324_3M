# Exercise 34 - Plot a function with matplotlib and argparse

## Prerequisites

1. Create a repository
2. Create a venv
3. Activate the venv
4. Install the required packages

## Exercise

In this exercise, you will use the `argparse` module to take command-line arguments and the `matplotlib` module to plot mathematical functions.

You will create a script named `plot_functions.py` that accepts a number `n` and one or more types of functions as arguments. The types of functions can be 'linear', 'polinomial', or 'exponential'.

The script should be able to be run like this:

``` bash
python plot_functions.py --linear --polinomial --exponential number
```

The functions to be plotted are as follows:

- Linear: y = n * x
- Polinomial: y = x^n
- Exponential: y = n^x

For each function specified, your script should generate a plot using matplotlib. The x-values should be an list of values between 0 and 10 (inclusive). The y-values should be calculated based on the function type and the input number n.

Remember to label the x-axis, y-axis, and provide a title for each plot. Display all the plots at the end.
