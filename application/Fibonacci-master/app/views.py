"""Views for the application."""

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    """Render the home page."""
    return render_template('index.html', title="Home")

@app.route('/test_script.html')
def test_script():
    """Render the test script page."""
    return render_template('test_script.html')

@app.route('/fib/')
def fib_usage():
    """Render the Fibonacci usage page."""
    return render_template('usage.html')

@app.route('/fib/<string:argument>')
def my_fib(argument):
    """Calculate Fibonacci numbers based on the input argument."""
    TRUNCATE_AFTER_THIS_MANY = 10000
    
    # Validate input
    try:
        number = int(float(argument))  # Float handles scientific notation
    except:
        message = "Could not interpret " + argument + " as an integer.  Please enter a positive integer in the url."
        return render_template('usage.html', msg = message)
    if number < 0:  # Check for negative input
        message = "Invalid input. " + str(number) + " must be a positive integer. Please try again."
        return render_template('usage.html', msg = message)
    
    def fib_list(num):
        """Generate a list of Fibonacci numbers up to num."""
        fib_numbers = []
        message = ""
        if num >= 1:  # First Fibonacci number
            fib_numbers.append(0)
        if num >= 2:  # Second Fibonacci number
            fib_numbers.append(1)
        if num > 2:  # More than two Fibonacci numbers
            if num > TRUNCATE_AFTER_THIS_MANY:  # Truncate if necessary
                num = TRUNCATE_AFTER_THIS_MANY
                message = "Truncated output after " + str(int(TRUNCATE_AFTER_THIS_MANY)) + " numbers."
            i=2
            while i <= num-1:  # -1 adjusts for zero-indexing
                fib_numbers.append( fib_numbers[i-2] + fib_numbers[i-1] )
                i += 1
        if num < 0:  # Check for negative input again
            message = "Invalid input. " + str(num) + " should be a positive integer."
            raise ValueError(message)
        return (fib_numbers, message)

    fibs = fib_list(number)
    return render_template('output.html', num=number, list=fibs[0], msg = fibs[1])