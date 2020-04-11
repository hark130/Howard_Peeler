# Standard Imports
from enum import Enum
import datetime
import sys
# Third Party Imports
# Local Imports

class Log_Cats(Enum):
    EMERG=1   # System is unusable
    ALERT=2   # Action must be taken immediately
    CRIT=3    # Critical conditions
    ERR=4     # Error conditions
    WARN=5    # Warning conditions
    NOTICE=6  # Normal, but significant, condition
    INFO=7    # Informational message
    DEBUG=8   # Debug-level message


def log_a_string(message, category=Log_Cats.INFO):
    """
        PURPOSE - Log a string to the console
        PARAMETERS
            message - Non-empty string to log
            category - Log_Cats name
    """
    # LOCAL VARIABLES
    formatted_message = ''

    # INPUT VALIDATION
    # message
    if not isinstance(message, str):
        raise TypeError(f'The message parameter must be a string instead of {type(message)}')
    elif not message:
        raise ValueError('The message parameter can not be empty')
    # category
    if not isinstance(category, Log_Cats):
        raise TypeError('The category parameter must be a Log_Cats name instead of '
                        f'{type(category)}')

    # LOG IT
    # Format it
    formatted_message += get_datestamp() + ' '
    formatted_message += get_timestamp() + ' '
    formatted_message += '[' + category.name + '] '
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
