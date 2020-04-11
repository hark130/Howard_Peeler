# Standard Imports
# Third Party Imports
# Local Imports
from HOPE_Logger import log_a_string, Log_Cats


def main():
    log_a_string("HOPE Start", Log_Cats.INFO)
    log_a_string("HOPE Stop", Log_Cats.INFO)


if __name__ == "__main__":
    main()
