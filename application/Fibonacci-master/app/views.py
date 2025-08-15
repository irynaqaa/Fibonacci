from flask import render_template
from app import app


@app.route('/'
)
@app.route('/index'
)
def index():
    """Render the index.html template with the title 'Home'."""
    return render_template('index.html', title="Home")


@app.route('/test_script.html'
)
def test_script():
    """Render the test_script.html template."""
    return render_template('test_script.html')


@app.route('/fib/'
)
def fib_usage():
    """Render the usage.html template."""
    return render_template('usage.html')


@app.route('/fib/<string:argument>'
)
def my_fib(argument):
    """Render the output.html template with the Fibonacci sequence.
    
    Args:
        argument (str): The input number as a string.
    """
    truncate_after_this_many = 1e4
    
    # Validate input
    try:
        number = int(float(argument))  # Float handles scientific notation
    except:
        message = "Could not interpret " + argument + " as an integer.  Please enter a positive integer in the url."
        return render_template('usage.html', msg = message)
    if number < 0:
        message = "Invalid input. " + str(number) + " must be a positive integer. Please try again."
        return render_template('usage.html', msg = message)
    
    def fib_list(num):
        """Generate the Fibonacci sequence up to the given number.
        
        Args:
            num (int): The input number.
        
        Returns:
            tuple: A tuple containing the Fibonacci sequence and a message.
        """
        fib_numbers = []
        message = ""
        
        if num >= 1:
            fib_numbers.append(0)
        if num >= 2:
            fib_numbers.append(1)
        if num > 2:  # assert: fib_numbers = [0, 1]
            if num > truncate_after_this_many:
                num = truncate_after_this_many
                message = "Truncated output after " + str(int(truncate_after_this_many)) + " numbers."
            i=2
            while i <= num-1:  # -1 adjusts for zero-indexing
                fib_numbers.append( fib_numbers[i-2] + fib_numbers[i-1] )
                i += 1
        if num < 0:
            message = "Invalid input. " + str(num) + " should be a positive integer."
            raise ValueError(message)
        
        return (fib_numbers, message)
    
    #return 'First %d Fibonacci numbers: %s' % (number, fib_list(number))
    fibs = fib_list(number)
    return render_template('output.html', num=number, list=fibs[0], msg = fibs[1])
