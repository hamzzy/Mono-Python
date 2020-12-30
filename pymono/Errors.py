class PyMonoError(Exception):
    """
    Python Paystack Error
    """
    pass


class MissingAuthKeyError(PyMonoError):
    """
    We can't find the authentication key
    """
    pass


class InvalidMethodError(PyMonoError):
    """
    Invalid or unrecoginised/unimplemented HTTP request method
    """
    pass


class Error(PyMonoError):
    """
     Random exception  taker
     """
    pass
