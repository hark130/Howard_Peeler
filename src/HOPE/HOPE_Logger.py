# Standard Imports
import datetime
import sys
# Third Party Imports
# Local Imports


def log_a_string(message):
    """
        PURPOSE - Log a string to the console
        PARAMETERS
            message - Non-empty string to log
    """
    # LOCAL VARIABLES
    formatted_message = ''

    # INPUT VALIDATION
    if not isinstance(message, str):
        raise TypeError(f'The message parameter must be a string instead of {type(message)}')
    elif not message:
        raise ValueError('The message parameter can not be empty')

    # LOG IT
    # Format it
    formatted_message += get_datestamp() + ' '
    formatted_message += get_timestamp() + ' '
    formatted_message += message
    # Log it
    print(formatted_message, file=sys.stdout)


def get_datestamp():
    """
        PURPOSE - Return the time as HH:MM:SS
        RETURN - String representation of today's date in YYY:MM:DD
    """
    return '{:%Y-%m-%d}'.format(datetime.datetime.now())


def get_timestamp():
    """
        PURPOSE - Return the date as HH:MM:SS
        RETURN - String representation of the current time in HH:MM:SS
    """
    return '{:%H:%M:%S}'.format(datetime.datetime.now())
