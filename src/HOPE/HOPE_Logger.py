import sys

def log_a_string(message):
    """
        PURPOSE - Log a string to the console
        PARAMETERS
            message - Non-empty string to log
    """
    # LOCAL VARIABLES

    # INPUT VALIDATION
    if not isinstance(message, str):
        raise TypeError(f'The message parameter must be a string instead of {type(message)}')
    elif not message:
        raise ValueError('The message parameter can not be empty')

    # LOG IT
    print(message, file=sys.stdout)    
