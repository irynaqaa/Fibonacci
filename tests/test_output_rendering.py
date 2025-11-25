import pytest
from application.fibonacci import render_output


def test_render_output():
    """Test output rendering with valid Fibonacci numbers."""
    fib_numbers = [0, 1, 1, 2, 3, 5]
    message = "Fibonacci numbers generated successfully"
    rendered = render_output(fib_numbers, message)
    assert "Fibonacci Numbers" in rendered
    assert "Fibonacci numbers generated successfully" in rendered
    assert "0" in rendered
    assert "5" in rendered
