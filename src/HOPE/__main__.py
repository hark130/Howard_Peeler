# Standard Imports
# Third Party Imports
# Local Imports
from HOPE_Logger import log_a_string, Log_Cats
from HOPE_Obfuscation import obfuscate_string
from HOPE_Subprocess import execute_command


def main():
    # ENTRANCE
    log_a_string('HOPE Start', Log_Cats.INFO)

    # LOCAL VARIABLES
    mask = 'Howard_Peeler'
    obfuscated_URL = ' \x1b\x03\x11\x01^p\x7f\x12\x12\x1bK\x1a-\rY\x02\x1d\tp'
    clear_text_URL = ''

    # TEST
    try:
        log_a_string(execute_command(['espeak', '--version']), Log_Cats.DEBUG)
    except RuntimeError as err:
        log_a_string(repr(err), Log_Cats.DEBUG)

    # DEOBFUSCATE URL
    clear_text_URL = obfuscate_string(obfuscated_URL, mask)
    log_a_string('De-obfuscated: ' + clear_text_URL, Log_Cats.INFO)

    # DONE
    log_a_string('HOPE Stop', Log_Cats.INFO)


if __name__ == "__main__":
    main()
