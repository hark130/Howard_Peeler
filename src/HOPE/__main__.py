# Standard Imports
# Third Party Imports
# Local Imports
from HOPE_Logger import log_a_string, Log_Cats
from HOPE_Obfuscation import obfuscate_string
from HOPE_Scraper import HOPE_Scraper
from HOPE_Scream import verify_espeak, HOPE_Scream
from HOPE_Subprocess import execute_command

# GLOBALS
# http://www.whoishostingthis.com/tools/user-agent/
USER_AGENTS = [
    # Actual (laptop)
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)',
    # https://docs.python.org/3/library/urllib.request.html
    'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) ' + \
    'Chrome/51.0.2704.84 Safari/537.36',
    # Chrome for Android (mobile & tablet)
    'Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/',
    # Chrome for iOS
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 ' + \
    '(KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
    # Chrome WebView (KitKat to Lollipop)
    'Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 ' + \
    '(KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
    # Chrome WebView (Lollipop and above)
    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 ' + \
    '(KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
]


def main():
    # ENTRANCE
    log_a_string('HOPE Start', Log_Cats.INFO)

    # LOCAL VARIABLES
    mask = 'Howard_Peeler'
    obfuscated_URL = ' \x1b\x03\x11\x01^p\x7f\x12\x12\x1bK\x1a-\rY\x02\x1d\tp'
    clear_text_URL = ''
    scream_obj = None
    scraper_obj = None

    # DEOBFUSCATE URL
    clear_text_URL = obfuscate_string(obfuscated_URL, mask)
    log_a_string('De-obfuscated: ' + clear_text_URL, Log_Cats.INFO)

    # ESPEAK
    scream_obj = HOPE_Scream()
    scream_obj.speak('This is a TEST')

    # URL
    scraper_obj = HOPE_Scraper(clear_text_URL)
    scraper_obj.do_it()
    print(scraper_obj.get_html_string())

    # DONE
    log_a_string('HOPE Stop', Log_Cats.INFO)


if __name__ == "__main__":
    main()
