"""
Creating a custom error by extending the TypeError class
"""


class MyCustomError(TypeError):
    """
    Raising a custom error by extending the TypeError class
    """

    def __init__(self, error_message, error_code):
        super().__init__(f'Error code: {error_code}, Error Message: {error_message}')
        self.message = error_message
        self.code = error_code


raise MyCustomError('This is a custom error', 403)
