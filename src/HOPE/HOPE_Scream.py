# Standard Imports
import subprocess
import time
# Third Party Imports
# Local Imports
from HOPE_Logger import log_a_string, Log_Cats
from HOPE_Subprocess import execute_command


def verify_espeak():
    """
        PURPOSE - Verify espeak is installed
        RETURNS True if espeak is installed
    """
    # LOCAL VARIABLES
    installed = True
    version_output = ''

    # CHECK IT
    try:
        version_output = execute_command(['espeak', '--version'])
    except Exception:
        installed = False
        log_a_string('espeak is not installed', Log_Cats.ERR)
    else:
        log_a_string(version_output, Log_Cats.DEBUG)

    # DONE
    return False  # FUNCTIONAL TESTING
    return installed


def verify_tput():
    """
        PURPOSE - Verify tput is installed
        RETURNS True if tput is installed
    """
    # LOCAL VARIABLES
    installed = True
    command_output = ''

    # CHECK IT
    try:
        command_output = execute_command(['tput', '-V'])
    except Exception:
        installed = False
        log_a_string('tput is not installed', Log_Cats.ERR)
    else:
        log_a_string(command_output, Log_Cats.DEBUG)

    # DONE
    # return False  # FUNCTIONAL TESTING
    return installed


"""
    PURPOSE - Make a sound.  Hopefully, speech.  Otherwise, some beeps.
    NOTES
        - This class implements the following methods, in order, to alert the caller:
            1. HOPE_Scream.speak(message) --> espeak message
            2. HOPE_Scream.speak(message) --> tput bel
            3. HOPE_Scream.speak(message) --> [DEBUG] message
"""
class HOPE_Scream:

    def __init__(self):
        # ATTRIBUTES
        # self._espeak_installed
        self._espeak_installed = verify_espeak()
        # self._espeak_config_obj
        if self._espeak_installed:
            self._espeak_config_obj = Espeak_Config()
        else:
            self._espeak_config_obj = None
        # self._tput_installed
        self._tput_installed = verify_tput()

    def speak(self, words):
        # INPUT VALIDATION
        self._validate_attributes(words)

        # LEARN TO SPEAK
        if self._espeak_installed:
            self._espeak_config_obj.speak(words)
        elif self._tput_installed:
            self._tput_it(words)
        else:
            log_a_string(words, Log_Cats.NOTICE)

    def _validate_attributes(self, words):
        # INPUT VALIDATION
        # self._words
        self._validate_words(words)

        # self._espeak_installed
        if not isinstance(self._espeak_installed, bool):
            raise TypeError('The _espeak_installed must be a bool instead of '
                            f'{type(self._espeak_installed)}')

        # self._espeak_config_obj
        if self._espeak_installed and not self._espeak_config_obj:
            raise RuntimeError('Espeak is installed but there is no Espeak_Config object')

        # self._tput_installed
        if not isinstance(self._tput_installed, bool):
            raise TypeError('The _tput_installed must be a bool instead of '
                            f'{type(self._tput_installed)}')

    def _validate_words(self, words):
        # VALIDATION
        if not isinstance(words, str):
            raise TypeError('The words parameter must be a string instead of '
                            f'{type(words)}')
        elif not words:
            raise ValueError('The words parameter may not be empty')

    def _tput_it(self, words):
        """
            PURPOSE - Converts a string into system beeps.  One beep per word.
            PARAMETERS
                words - Non-empty string to convert into beeps
            NOTES
                - Implements "tput bel" under the hood
        """
        # LOCAL VARIABLES
        default_command_list = ['tput']
        bell_string = 'bel'
        command_list = default_command_list + [bell_string]

        # EXECUTE COMMAND LIST
        for _ in range(len(words.split())):
            log_a_string(f'HOPE_Scream is executing {repr(command_list)}', Log_Cats.DEBUG)  # DEBUGGING
            subprocess.run(command_list)
            time.sleep(.1)


class Espeak_Config:

    def __init__(self, amplitude=None, word_gap=None, capitals='20',
                 line_length=None, pitch=None, wpms=None):
        # ATTRIBUTES
        self._amp = amplitude
        self._word_gap = word_gap
        self._capitals = capitals
        self._line_len = line_length
        self._pitch = pitch
        self._wpms = wpms
        self._string_delims = ["'", '"']

    def speak(self, words):
        # VALIDATION
        # Attributes
        self._validate_attributes()
        # words
        self._validate_words(words)

        # LOCAL VARIABLES
        command_list = self._create_command_list(words)

        # EXECUTE COMMAND LIST
        execute_command(command_list)

    def _validate_attributes(self):
        """
            PURPOSE - Validates the content of internal attributes
        """
        # VALIDATION
        # _amp
        if self._amp is not None and not isinstance(self._amp, str):
            raise ValueError('The amplitude parameter was invalid')
        # _word_gap
        if self._word_gap is not None and not isinstance(self._word_gap, str):
            raise ValueError('The word_gap parameter was invalid')
        # _capitals
        if self._capitals is not None and not isinstance(self._capitals, str):
            raise ValueError('The captials parameter was invalid')
        # _line_len
        if self._line_len is not None and not isinstance(self._line_len, str):
            raise ValueError('The line_length parameter was invalid')
        # _pitch
        if self._pitch is not None and not isinstance(self._pitch, str):
            raise ValueError('The pitch parameter was invalid')
        # _wpms
        if self._wpms is not None and not isinstance(self._wpms, str):
            raise ValueError('The wpms parameter was invalid')

    def _validate_words(self, words):
        # VALIDATION
        if not isinstance(words, str):
            raise TypeError('The words parameter must be a string instead of '
                            f'{type(words)}')
        elif not words:
            raise ValueError('The words parameter may not be empty')

    def _create_command_list(self, words):
        """
            PURPOSE - Builds the espeak command list based on attributes
            RETURNS a list of strings
        """
        # LOCAL VARIABLES
        command_list = ['espeak']
        string_delims = self._string_delims
        wrapped_words = words
        needs_wrapping = True
        wrapped_it = False

        # VALIDATION
        # Attributes
        self._validate_attributes()
        # words
        self._validate_words(words)

        # BUILD COMMAND LIST
        # _amp
        if self._amp:
            command_list.append('-a' + self._amp)

        # _word_gap
        if self._word_gap:
            command_list.append('-g' + self._word_gap)

        # _capitals
        if self._capitals:
            command_list.append('-k' + self._capitals)

        # _line_len
        if self._line_len:
            command_list.append('-l' + self._line_len)

        # _pitch
        if self._pitch:
            command_list.append('-p' + self._pitch)

        # _wpms
        if self._wpms:
            command_list.append('-s' + self._wpms)

        # words
        for delim in string_delims:
            if wrapped_words.startswith(delim) and wrapped_words.endswith(delim):
                needs_wrapping = False
                break
        if needs_wrapping:
            for delim in string_delims:
                if delim not in wrapped_words:
                    wrapped_words = delim + wrapped_words + delim
                    wrapped_it = True
                    break
            if not wrapped_it:
                raise RuntimeError(f'Somehow "{words}" incorporates both string delimiters')
        command_list.append(wrapped_words)

        # DONE
        return command_list
