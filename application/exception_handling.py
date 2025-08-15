"""
Module to handle exceptions.
"""


class AuthenticationError(Exception):
    """
    Authentication error exception.

    Attributes:
        message (str): The error message.
    """
    def __init__(self, message):
        """
        Initialize the exception.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(message)
