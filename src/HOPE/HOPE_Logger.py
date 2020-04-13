# Standard Imports
from enum import Enum
import datetime
import sys
# Third Party Imports
# Local Imports

__DEBUG__ = True


class Log_Cats(Enum):
    EMERG = 1   # System is unusable
    ALERT = 2   # Action must be taken immediately
    CRIT = 3    # Critical conditions
    ERR = 4     # Error conditions
    WARN = 5    # Warning conditions
    NOTICE = 6  # Normal, but significant, condition
    INFO = 7    # Informational message
    DEBUG = 8   # Debug-level message


def log_a_string(message, category=Log_Cats.INFO):
    """
        PURPOSE - Log a string to the console
        PARAMETERS
            message - Non-empty string to log
            category - Log_Cats name
    """
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

    # LOCAL VARIABLES
    formatted_message = ''
    stripped_message = strip_newlines(message)
    print_it = False

    # CHECK DEBUG STATUS
    if __DEBUG__:
        print_it = True
    elif category.name != Log_Cats.DEBUG.name:
        print_it = True

    if print_it:
        # LOG IT
        # Format it
        formatted_message += get_datestamp() + ' '
        formatted_message += get_timestamp() + ' '
        formatted_message += '[' + category.name + '] '
        formatted_message += stripped_message
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


def strip_newlines(string_to_strip):
    """
        PURPOSE - Strip all newline characters from a string
        PARAMETERS
            string_to_strip - String, empty or otherwise, from which to strip newlines
        RETURN - string_to_strip with all newlines removed
    """
    # INPUT VALIDATION

    # LOCAL VARIABLES
    strings_to_replace = ['\n', '\r\n']
    stripped_string = string_to_strip
    new_char = ' '  # Replace with this character

    # STRIP IT
    for string_to_replace in strings_to_replace:
        stripped_string = stripped_string.replace(string_to_replace,
                                                  new_char * len(string_to_replace))

    # DONE
    return stripped_string
